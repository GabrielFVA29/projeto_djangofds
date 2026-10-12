"""
Views do Simulador de Decisões IoT.

Fluxo de telas (planejamento do time de design):
  T1 inicio -> T2 como_funciona -> T4 cenario -> T5 resultado -> ... -> T7 relatorio
  (T3 "escolha sua trilha" e T6 "progresso" entram na Entrega 04.)

Regras da disciplina seguidas aqui:
- Só views em função (sem generic views).
- Sem Django Forms: os dados vêm direto de request.POST e são validados à mão.
- Todas as histórias leem e/ou gravam no banco de dados.
"""
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Cenario, Decisao, Opcao, Rodada

# Na sessão guardamos só o id da rodada atual; as decisões ficam no banco.
CHAVE_RODADA = "simulador_rodada_id"

TAMANHO_MAXIMO_NOME = 80
NOME_TRILHA = "Trilha geral"  # na Entrega 04 vem da escolha de trilha (T3)


# ---------------------------------------------------------------- utilidades

def reais(valor):
    """Formata um número como dinheiro: 1500 -> 'R$ 1.500'."""
    texto = f"{abs(valor):,.0f}".replace(",", ".")
    sinal = "-" if valor < 0 else ""
    return f"{sinal}R$ {texto}"


def pontos_de_progresso(concluidos, total, atual=None):
    """Lista usada para desenhar os 'dots' de progresso das telas."""
    pontos = []
    for numero in range(1, total + 1):
        if numero <= concluidos:
            estado = "feito"
        elif numero == atual:
            estado = "atual"
        else:
            estado = "vazio"
        pontos.append(estado)
    return pontos


def metricas(perda_restante, custo):
    """Três métricas de um card (prejuízo que continua, custo e resultado)."""
    return {
        "perda_restante_fmt": reais(perda_restante),
        "custo_fmt": reais(custo),
    }


def impacto(opcao):
    """Impacto financeiro de uma alternativa, já formatado para o template."""
    return {
        **metricas(opcao.perda_restante, opcao.custo),
        "resultado": opcao.resultado,
        "resultado_fmt": reais(opcao.resultado),
        "positivo": opcao.resultado > 0,
    }


def rodada_atual(request):
    """Rodada guardada na sessão deste navegador (ou None)."""
    rodada_id = request.session.get(CHAVE_RODADA)
    if rodada_id is None:
        return None
    return Rodada.objects.filter(id=rodada_id).first()


def proximo_cenario_pendente(rodada):
    """Primeiro cenário que a rodada ainda não respondeu (ou None)."""
    respondidos = rodada.decisoes.values_list("cenario_id", flat=True)
    return Cenario.objects.exclude(id__in=list(respondidos)).first()


def minutos_estimados(total_cenarios):
    """Tempo estimado da simulação (cerca de 1 minuto por rodada + leitura)."""
    return max(3, total_cenarios + 1)


# ------------------------------------------------- T1 e T2 (História 2)

def inicio(request):
    """T1: tela de abertura do simulador."""
    total = Cenario.objects.count()
    return render(request, "simulador/inicio.html", {
        "total": total,
        "minutos": minutos_estimados(total),
        "rodada": rodada_atual(request),
    })


def _tela_como_funciona(request, erros=None, valores=None):
    total = Cenario.objects.count()
    return render(request, "simulador/como_funciona.html", {
        "total": total,
        "minutos": minutos_estimados(total),
        "pontos": pontos_de_progresso(0, total),
        "erros": erros or [],
        "valores": valores or {},
    })


def como_funciona(request):
    """T2: explica as etapas, como o desempenho é calculado e pede nome/empresa."""
    return _tela_como_funciona(request)


def comecar(request):
    """Recebe nome e empresa (sem Django Forms), cria a rodada e vai à 1ª rodada."""
    if request.method != "POST":
        return redirect("simulador:como_funciona")

    jogador = request.POST.get("jogador", "").strip()
    empresa = request.POST.get("empresa", "").strip()

    erros = []
    if not jogador:
        erros.append("Informe o seu nome.")
    if not empresa:
        erros.append("Informe o nome da empresa.")
    if len(jogador) > TAMANHO_MAXIMO_NOME or len(empresa) > TAMANHO_MAXIMO_NOME:
        erros.append(f"Use no máximo {TAMANHO_MAXIMO_NOME} caracteres em cada campo.")

    if erros:
        return _tela_como_funciona(request, erros, {"jogador": jogador, "empresa": empresa})

    rodada = Rodada.objects.create(jogador=jogador, empresa=empresa)
    request.session[CHAVE_RODADA] = rodada.id

    primeiro = Cenario.objects.first()
    if primeiro is None:
        raise Http404("Nenhum cenário cadastrado.")
    return redirect("simulador:cenario", numero=primeiro.numero)


# ------------------------------------------------- T4 e T5 (História 1)

def cenario(request, numero):
    """
    T4. GET: mostra a situação, as vozes da equipe e as alternativas.
    POST: grava a decisão escolhida no banco e leva à consequência (T5).
    """
    rodada = rodada_atual(request)
    if rodada is None:
        return redirect("simulador:inicio")

    cenario_atual = get_object_or_404(Cenario, numero=numero)
    erro = None

    if request.method == "POST":
        letra = request.POST.get("opcao", "")
        opcao = Opcao.objects.filter(cenario=cenario_atual, letra=letra).first()
        if opcao is not None:
            Decisao.objects.update_or_create(
                rodada=rodada,
                cenario=cenario_atual,
                defaults={"opcao": opcao},
            )
            return redirect("simulador:resultado", numero=numero)
        erro = "Escolha uma das alternativas para continuar."

    total = Cenario.objects.count()
    posicao = Cenario.objects.filter(numero__lt=numero).count() + 1
    return render(request, "simulador/cenario.html", {
        "cenario": cenario_atual,
        "vozes": cenario_atual.vozes.all(),
        "opcoes": [
            {"letra": o.letra, "texto": o.texto, "custo_fmt": reais(o.custo)}
            for o in cenario_atual.opcoes.all()
        ],
        "posicao": posicao,
        "total": total,
        "trilha": NOME_TRILHA,
        "pontos": pontos_de_progresso(posicao - 1, total, atual=posicao),
        "perda_atual_fmt": reais(cenario_atual.perda_atual),
        "erro": erro,
    })


def resultado(request, numero):
    """T5: consequência da decisão, comparando sem IoT × com IoT."""
    rodada = rodada_atual(request)
    if rodada is None:
        return redirect("simulador:inicio")

    cenario_atual = get_object_or_404(Cenario, numero=numero)
    decisao = Decisao.objects.filter(rodada=rodada, cenario=cenario_atual).select_related("opcao").first()
    if decisao is None:
        return redirect("simulador:cenario", numero=numero)

    escolha = decisao.opcao
    iot = cenario_atual.opcao_iot()

    if escolha.usa_iot or iot is None:
        # Escolheu IoT: compara com a situação de antes, sem dados.
        comparacao = {
            "titulo": "Sem dados · Como estava",
            "texto": "Sem nenhuma mudança, o problema continuava custando isso todo mês.",
            **metricas(cenario_atual.perda_atual, 0),
            "resultado_fmt": reais(0),
            "positivo": False,
            "tipo": "sem",
        }
        ganho_extra = escolha.resultado
        texto_ganho = "Prejuízo evitado com a sua decisão"
    else:
        comparacao = {
            "titulo": "Com IoT · O que mudaria",
            "texto": iot.texto,
            **impacto(iot),
            "tipo": "com",
        }
        ganho_extra = iot.resultado - escolha.resultado
        texto_ganho = "Prejuízo a mais que a IoT evitaria"

    proximo = Cenario.objects.filter(numero__gt=numero).first()
    total = Cenario.objects.count()
    posicao = Cenario.objects.filter(numero__lte=numero).count()

    return render(request, "simulador/resultado.html", {
        "cenario": cenario_atual,
        "escolha": escolha,
        "impacto": impacto(escolha),
        "iot": iot,
        "comparacao": comparacao,
        "ganho_extra_fmt": reais(max(0, ganho_extra)),
        "texto_ganho": texto_ganho,
        "posicao": posicao,
        "total": total,
        "trilha": NOME_TRILHA,
        "pontos": pontos_de_progresso(posicao, total),
        "proximo": proximo,
    })


# ------------------------------------------------- T7 (História 1)

def _montar_relatorio(request, rodada, eh_meu):
    itens = []
    sua = {"perda": 0, "custo": 0, "resultado": 0}
    bzu = {"perda": 0, "custo": 0, "resultado": 0}

    for decisao in rodada.decisoes.select_related("cenario", "opcao__cenario"):
        escolha = decisao.opcao
        iot = decisao.cenario.opcao_iot() or escolha
        sua["perda"] += escolha.perda_restante
        sua["custo"] += escolha.custo
        sua["resultado"] += escolha.resultado
        bzu["perda"] += iot.perda_restante
        bzu["custo"] += iot.custo
        bzu["resultado"] += iot.resultado
        itens.append({
            "cenario": decisao.cenario,
            "escolha": escolha,
            "impacto": impacto(escolha),
            "impacto_iot": impacto(iot),
        })

    diferenca = bzu["resultado"] - sua["resultado"]
    return render(request, "simulador/relatorio.html", {
        "rodada": rodada,
        "eh_meu": eh_meu,
        "itens": itens,
        "total": len(itens),
        "acertos_iot": rodada.decisoes_iot(),
        "pontuacao": rodada.pontuacao(),
        "sua": {
            "perda_fmt": reais(sua["perda"]),
            "custo_fmt": reais(sua["custo"]),
            "resultado_fmt": reais(sua["resultado"]),
        },
        "bzu": {
            "perda_fmt": reais(bzu["perda"]),
            "custo_fmt": reais(bzu["custo"]),
            "resultado_fmt": reais(bzu["resultado"]),
        },
        "resultado_anual_fmt": reais(sua["resultado"] * 12),
        "resultado_positivo": sua["resultado"] > 0,
        "diferenca": diferenca,
        "diferenca_fmt": reais(diferenca),
        "diferenca_anual_fmt": reais(diferenca * 12),
    })


def relatorio(request):
    """T7: resultado final da rodada atual. Marca a rodada como finalizada."""
    rodada = rodada_atual(request)
    if rodada is None:
        return redirect("simulador:inicio")

    pendente = proximo_cenario_pendente(rodada)
    if pendente is not None:
        return redirect("simulador:cenario", numero=pendente.numero)

    if not rodada.finalizada:
        rodada.finalizada_em = timezone.now()
        rodada.save(update_fields=["finalizada_em"])

    return _montar_relatorio(request, rodada, eh_meu=True)


# ------------------------------------------------- Ranking (História 3)

def ranking(request):
    """Ranking das rodadas finalizadas por toda a equipe."""
    linhas = []
    for rodada in Rodada.objects.filter(finalizada_em__isnull=False):
        resultado_total = rodada.resultado_total()
        linhas.append({
            "rodada": rodada,
            "pontuacao": rodada.pontuacao(),
            "decisoes_iot": rodada.decisoes_iot(),
            "resultado_fmt": reais(resultado_total),
            "positivo": resultado_total > 0,
        })
    linhas.sort(key=lambda linha: (-linha["pontuacao"], linha["rodada"].finalizada_em))

    for posicao, linha in enumerate(linhas, start=1):
        linha["posicao"] = posicao

    minha = rodada_atual(request)
    return render(request, "simulador/ranking.html", {
        "linhas": linhas,
        "total_cenarios": Cenario.objects.count(),
        "minha_rodada_id": minha.id if minha else None,
    })


def rodada_detalhe(request, rodada_id):
    """Resultado final de uma rodada finalizada de outra pessoa (vindo do ranking)."""
    rodada = get_object_or_404(Rodada, id=rodada_id, finalizada_em__isnull=False)
    minha = rodada_atual(request)
    return _montar_relatorio(request, rodada, eh_meu=(minha is not None and minha.id == rodada.id))
