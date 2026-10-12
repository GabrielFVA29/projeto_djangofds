"""
Testes das histórias implementadas na Entrega 03 (ver historias.md).
Cada classe corresponde a uma história e cada teste a um cenário BDD.

Para rodar:  python manage.py test simulador
O banco de teste é criado com as migrações, então os cenários iniciais
(migração 0002) já estão disponíveis.
"""
from django.test import TestCase
from django.urls import reverse

from .models import Cenario, Decisao, Rodada
from .views import CHAVE_RODADA, reais


class Base(TestCase):
    def comecar(self, jogador="João", empresa="Distribuidora Recife"):
        return self.client.post(reverse("simulador:comecar"), {"jogador": jogador, "empresa": empresa})

    def responder(self, numero, letra):
        return self.client.post(reverse("simulador:cenario", args=[numero]), {"opcao": letra})

    def jogar_rodada(self, usar_iot=False, **dados):
        self.comecar(**dados)
        for cenario in Cenario.objects.all():
            opcao = cenario.opcoes.filter(usa_iot=usar_iot).first()
            self.responder(cenario.numero, opcao.letra)
        return self.client.get(reverse("simulador:relatorio"))


# ---------------------------------------------------------------- História 1

class H1SimuladorDeDecisoesTest(Base):
    """História 1: simulador de decisões com IoT."""

    def test_cenarios_iniciais_estao_no_banco_e_todos_tem_opcao_iot(self):
        self.assertGreaterEqual(Cenario.objects.count(), 3)
        for cenario in Cenario.objects.all():
            self.assertGreaterEqual(cenario.opcoes.count(), 2)
            self.assertIsNotNone(cenario.opcao_iot(), f"Cenário {cenario.numero} sem opção IoT")

    def test_dado_que_comecei_entao_vejo_problema_vozes_e_alternativas(self):
        self.comecar()
        cenario = Cenario.objects.first()
        resposta = self.client.get(reverse("simulador:cenario", args=[cenario.numero]))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, cenario.titulo)
        self.assertContains(resposta, "Alex")
        for opcao in cenario.opcoes.all():
            self.assertContains(resposta, opcao.texto)

    def test_quando_clico_em_uma_alternativa_a_decisao_e_gravada_com_1_clique(self):
        self.comecar()
        resposta = self.responder(1, "b")
        self.assertRedirects(resposta, reverse("simulador:resultado", args=[1]))
        decisao = Decisao.objects.get()
        self.assertEqual(decisao.opcao.letra, "b")
        self.assertEqual(decisao.cenario.numero, 1)

    def test_decidir_leva_2_cliques_escolher_e_confirmar(self):
        # 1º clique: seleciona a alternativa (radio). 2º clique: "Confirmar decisão".
        self.comecar()
        resposta = self.client.get(reverse("simulador:cenario", args=[1]))
        total_opcoes = Cenario.objects.get(numero=1).opcoes.count()
        self.assertContains(resposta, 'type="radio" name="opcao"', count=total_opcoes)
        self.assertContains(resposta, "Confirmar decisão")
        self.assertContains(resposta, f"Rodada 1 de {Cenario.objects.count()}")

    def test_alternativa_invalida_mostra_mensagem_e_nao_grava(self):
        self.comecar()
        resposta = self.responder(1, "z")
        self.assertContains(resposta, "Escolha uma das alternativas")
        self.assertEqual(Decisao.objects.count(), 0)

    def test_mudar_de_ideia_atualiza_a_decisao_em_vez_de_duplicar(self):
        self.comecar()
        self.responder(1, "a")
        self.responder(1, "b")
        self.assertEqual(Decisao.objects.count(), 1)
        self.assertEqual(Decisao.objects.get().opcao.letra, "b")

    def test_quando_escolho_entao_vejo_o_impacto_financeiro_na_hora(self):
        self.comecar()
        resposta = self.client.post(reverse("simulador:cenario", args=[1]), {"opcao": "a"}, follow=True)
        opcao = Cenario.objects.get(numero=1).opcoes.get(letra="a")
        self.assertContains(resposta, "Veja o que aconteceu")
        self.assertContains(resposta, "Sem IoT · Sua decisão")
        self.assertContains(resposta, reais(opcao.custo))
        self.assertContains(resposta, reais(opcao.perda_restante))
        self.assertContains(resposta, reais(opcao.resultado))

    def test_calculo_do_resultado_financeiro(self):
        opcao = Cenario.objects.get(numero=1).opcoes.get(letra="a")  # 18.000 - 9.000 - 4.500
        self.assertEqual(opcao.economia, 9000)
        self.assertEqual(opcao.resultado, 4500)

    def test_quando_nao_escolho_iot_entao_vejo_como_a_iot_resolveria(self):
        self.comecar()
        cenario = Cenario.objects.get(numero=1)
        sem_iot = cenario.opcoes.filter(usa_iot=False).first()
        resposta = self.client.post(
            reverse("simulador:cenario", args=[1]), {"opcao": sem_iot.letra}, follow=True
        )
        self.assertContains(resposta, "Com IoT · O que mudaria")
        self.assertContains(resposta, cenario.opcao_iot().texto)

    def test_quando_escolho_iot_entao_comparo_com_a_situacao_sem_dados(self):
        self.comecar()
        cenario = Cenario.objects.get(numero=1)
        resposta = self.client.post(
            reverse("simulador:cenario", args=[1]), {"opcao": cenario.opcao_iot().letra}, follow=True
        )
        self.assertContains(resposta, "Com IoT · Sua decisão")
        self.assertContains(resposta, "Sem dados · Como estava")
        self.assertContains(resposta, reais(cenario.perda_atual))

    def test_resultado_sem_escolha_volta_para_o_cenario(self):
        self.comecar()
        resposta = self.client.get(reverse("simulador:resultado", args=[2]))
        self.assertRedirects(resposta, reverse("simulador:cenario", args=[2]))

    def test_relatorio_explica_o_conceito_de_cada_cenario(self):
        resposta = self.jogar_rodada()
        self.assertContains(resposta, "Veja o que a Bzu teria feito diferente")
        self.assertContains(resposta, "Sem IoT · Sua jornada")
        self.assertContains(resposta, "Com Bzu IoT · O que mudaria")
        for cenario in Cenario.objects.all():
            self.assertContains(resposta, cenario.conceito_titulo)
            self.assertContains(resposta, cenario.lista_passos[0])

    def test_relatorio_antes_de_terminar_leva_ao_cenario_que_falta(self):
        self.comecar()
        self.responder(1, "a")
        resposta = self.client.get(reverse("simulador:relatorio"))
        self.assertRedirects(resposta, reverse("simulador:cenario", args=[2]))

    def test_relatorio_marca_a_rodada_como_finalizada(self):
        self.jogar_rodada()
        self.assertIsNotNone(Rodada.objects.get().finalizada_em)

    def test_cenario_inexistente_retorna_404(self):
        self.comecar()
        resposta = self.client.get(reverse("simulador:cenario", args=[999]))
        self.assertEqual(resposta.status_code, 404)

    def test_relatorio_tem_botoes_saber_mais_e_refazer(self):
        resposta = self.jogar_rodada()
        self.assertContains(resposta, "Quero saber mais sobre a Bzu Tech")
        self.assertContains(resposta, "https://www.bzutech.com.br")
        self.assertContains(resposta, "Refazer simulação")

    def test_paginas_abrem_logo_apos_o_deploy_sem_cadastro_manual(self):
        for url in ["/", reverse("simulador:inicio"), reverse("simulador:como_funciona"), reverse("simulador:ranking")]:
            self.assertEqual(self.client.get(url).status_code, 200, url)


# ---------------------------------------------------------------- História 2

class H2IdentificacaoDoJogadorTest(Base):
    """História 2: identificar jogador e empresa antes de jogar."""

    def test_dado_nome_e_empresa_quando_comeco_entao_a_rodada_e_gravada(self):
        resposta = self.comecar("Maria", "Frigorífico Boa Vista")
        rodada = Rodada.objects.get()
        self.assertEqual(rodada.jogador, "Maria")
        self.assertEqual(rodada.empresa, "Frigorífico Boa Vista")
        self.assertEqual(self.client.session[CHAVE_RODADA], rodada.id)
        self.assertRedirects(resposta, reverse("simulador:cenario", args=[1]))

    def test_tela_como_funciona_explica_e_pede_nome_e_empresa(self):
        resposta = self.client.get(reverse("simulador:como_funciona"))
        self.assertContains(resposta, "Como seu desempenho é calculado")
        self.assertContains(resposta, 'name="jogador"')
        self.assertContains(resposta, 'name="empresa"')

    def test_inicio_leva_para_como_funciona(self):
        resposta = self.client.get(reverse("simulador:inicio"))
        self.assertContains(resposta, reverse("simulador:como_funciona"))
        self.assertContains(resposta, "Tempo estimado")

    def test_sem_nome_nao_comeca_e_mostra_erro(self):
        resposta = self.comecar("", "Empresa X")
        self.assertContains(resposta, "Informe o seu nome.")
        self.assertEqual(Rodada.objects.count(), 0)

    def test_sem_empresa_nao_comeca_e_mantem_o_nome_digitado(self):
        resposta = self.comecar("Maria", "   ")
        self.assertContains(resposta, "Informe o nome da empresa.")
        self.assertContains(resposta, 'value="Maria"')
        self.assertEqual(Rodada.objects.count(), 0)

    def test_nome_muito_longo_e_recusado(self):
        resposta = self.comecar("A" * 81, "Empresa X")
        self.assertContains(resposta, "no máximo 80 caracteres")
        self.assertEqual(Rodada.objects.count(), 0)

    def test_sem_se_identificar_nao_acessa_os_cenarios(self):
        resposta = self.client.get(reverse("simulador:cenario", args=[1]))
        self.assertRedirects(resposta, reverse("simulador:inicio"))

    def test_relatorio_mostra_o_nome_da_empresa(self):
        resposta = self.jogar_rodada(jogador="Maria", empresa="Frigorífico Boa Vista")
        self.assertContains(resposta, "Relatório de aprendizado da <strong>Frigorífico Boa Vista</strong>", html=False)
        self.assertContains(resposta, "<strong>Maria</strong>", html=False)

    def test_nova_rodada_nao_apaga_a_anterior(self):
        self.jogar_rodada(jogador="Maria")
        self.comecar("Maria", "Outra empresa")
        self.assertEqual(Rodada.objects.count(), 2)


# ---------------------------------------------------------------- História 3

class H3RankingDaEquipeTest(Base):
    """História 3: ranking das rodadas da equipe."""

    def test_ranking_vazio_mostra_convite(self):
        resposta = self.client.get(reverse("simulador:ranking"))
        self.assertContains(resposta, "Ninguém concluiu uma simulação ainda")

    def test_rodada_finalizada_aparece_no_ranking(self):
        self.jogar_rodada(jogador="Maria", empresa="Empresa M")
        resposta = self.client.get(reverse("simulador:ranking"))
        self.assertContains(resposta, "Maria")
        self.assertContains(resposta, "Empresa M")

    def test_rodada_em_andamento_nao_aparece_no_ranking(self):
        self.comecar("Pedro", "Empresa P")
        self.responder(1, "a")
        resposta = self.client.get(reverse("simulador:ranking"))
        self.assertNotContains(resposta, "Pedro")

    def test_ranking_ordena_pela_maior_pontuacao(self):
        self.jogar_rodada(usar_iot=False, jogador="Sem Dados")
        self.jogar_rodada(usar_iot=True, jogador="Com Dados")
        html = self.client.get(reverse("simulador:ranking")).content.decode()
        self.assertLess(html.index("Com Dados"), html.index("Sem Dados"))

    def test_pontuacao_maxima_quando_usa_iot_em_tudo(self):
        self.jogar_rodada(usar_iot=True)
        self.assertEqual(Rodada.objects.get().pontuacao(), 100)

    def test_clicar_numa_rodada_mostra_as_decisoes_dela(self):
        self.jogar_rodada(jogador="Maria", empresa="Empresa M")
        rodada = Rodada.objects.get()
        resposta = self.client.get(reverse("simulador:rodada", args=[rodada.id]))
        self.assertContains(resposta, "Relatório de aprendizado da <strong>Empresa M</strong>", html=False)
        primeira = rodada.decisoes.first()
        self.assertContains(resposta, primeira.opcao.texto)

    def test_rodada_nao_finalizada_nao_pode_ser_vista_pelo_ranking(self):
        self.comecar()
        rodada = Rodada.objects.get()
        resposta = self.client.get(reverse("simulador:rodada", args=[rodada.id]))
        self.assertEqual(resposta.status_code, 404)
