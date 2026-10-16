"""
Dados iniciais do Simulador de Decisões IoT.

Estes cenários são gravados no banco de dados automaticamente pela migração
0002_cenarios_iniciais (ao rodar `python manage.py migrate`). Assim o
simulador já funciona logo após o deploy, sem ninguém precisar cadastrar
nada (critério "Autonomia de funcionamento").

Valores em R$ por mês:
- perda_atual: quanto a empresa perde hoje com o problema.
- custo: quanto a alternativa custa por mês.
- perda_restante: quanto do problema continua depois da escolha.

São 6 trilhas (segmentos) com 5 rodadas cada. Cada cenário indica a sua
trilha ("trilha") e a sua posição dentro dela ("ordem").
"""

# Trilhas (segmentos) que o jogador escolhe na tela T3.
# "diagnostico" é o 1º parágrafo do card de diagnóstico no resultado final (T7).
TRILHAS = [
    {
        "numero": 1,
        "slug": "saude",
        "nome": "Saúde e Cadeia Fria",
        "icone": "saude",
        "descricao": "Hospitais, clínicas, farmácias e distribuidoras que dependem de temperatura controlada e de equipamentos sempre à mão.",
        "exemplos": "Câmaras frias, vacinas, transporte de remédios, oxigênio",
        "diagnostico": (
            "Na saúde, um problema descoberto tarde não custa só dinheiro: pode "
            "significar uma vacina perdida ou um paciente esperando. Por isso, "
            "nesse segmento, saber o que está acontecendo em tempo real vale mais "
            "do que ter equipamento sobrando."
        ),
    },
    {
        "numero": 2,
        "slug": "industria",
        "nome": "Indústria e Manufatura",
        "icone": "industria",
        "descricao": "Fábricas em que cada minuto de máquina parada ou peça com defeito vira prejuízo.",
        "exemplos": "Prensas, injetoras, compressores, energia da fábrica",
        "diagnostico": (
            "Na indústria, o prejuízo costuma estar escondido em pequenas perdas "
            "que ninguém mede: alguns minutos de parada, um vazamento silencioso, "
            "um molde fora do ponto. Quando essas perdas viram números, a fábrica "
            "produz mais com as mesmas máquinas."
        ),
    },
    {
        "numero": 3,
        "slug": "logistica",
        "nome": "Logística e Varejo",
        "icone": "logistica",
        "descricao": "Empresas que movimentam mercadorias, fazem entregas e atendem clientes em lojas.",
        "exemplos": "Frota de caminhões, armazéns, entregas, supermercados",
        "diagnostico": (
            "Em logística e varejo, tudo está em movimento: caminhões, paletes, "
            "produtos e clientes. Quem enxerga esse movimento em tempo real "
            "consegue colocar a pessoa certa, no lugar certo, na hora certa, sem "
            "precisar aumentar a equipe ou a frota."
        ),
    },
    {
        "numero": 4,
        "slug": "predial",
        "nome": "Infraestrutura Predial",
        "icone": "predio",
        "descricao": "Prédios comerciais, condomínios e escritórios que gastam com energia, água e manutenção.",
        "exemplos": "Ar-condicionado, água, elevadores, quadros elétricos",
        "diagnostico": (
            "Em prédios, boa parte dos gastos acontece quando ninguém está olhando: "
            "de madrugada, nos fins de semana, dentro das paredes. Sensores "
            "transformam o prédio em algo que avisa os próprios problemas, antes "
            "que virem conta alta ou equipamento quebrado."
        ),
    },
    {
        "numero": 5,
        "slug": "publica",
        "nome": "Educação e Gestão Pública",
        "icone": "educacao",
        "descricao": "Prefeituras, escolas e serviços públicos que precisam cuidar bem do dinheiro do contribuinte.",
        "exemplos": "Iluminação pública, escolas, coleta de lixo, ônibus, alagamentos",
        "diagnostico": (
            "Na gestão pública, a escala é grande: são milhares de postes, dezenas "
            "de escolas e bairros inteiros. Decidir com dados permite gastar o "
            "dinheiro público onde ele realmente faz diferença e atender a "
            "população antes que ela precise reclamar."
        ),
    },
    {
        "numero": 6,
        "slug": "agro",
        "nome": "Agronegócio",
        "icone": "agro",
        "descricao": "Fazendas e cooperativas em que clima, solo e animais mudam todos os dias.",
        "exemplos": "Irrigação, silos de grãos, gado leiteiro, estufas, pragas",
        "diagnostico": (
            "No campo, a experiência do produtor é muito valiosa, mas a fazenda é "
            "grande demais para ser vista inteira todos os dias. Os sensores "
            "funcionam como olhos espalhados pela propriedade e confirmam com "
            "números o que o produtor sente."
        ),
    },
]

CENARIOS = [
    {
        "numero": 1,
        "trilha": "saude",
        "ordem": 1,
        "setor": "Cadeia fria",
        "titulo": "A câmara fria que estraga produtos",
        "problema": (
            "Sua distribuidora de alimentos está jogando fora carnes e laticínios "
            "toda semana. A câmara fria parece funcionar, mas de manhã alguns "
            "lotes amanhecem fora da temperatura ideal. Ninguém sabe dizer a que "
            "horas o problema acontece."
        ),
        "perda_atual": 18000,
        "vozes": [
            {
                "nome": "Marta",
                "papel": "Gerente de operações",
                "fala": "Essa câmara é velha. Na minha opinião, é só trocar por uma nova.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Antes de gastar, precisamos saber QUANDO e POR QUE a temperatura "
                    "sobe. Sem dado, qualquer solução é chute."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Contratar um vigia noturno para conferir o termômetro a cada 2 horas",
                "custo": 4500,
                "perda_restante": 9000,
                "iot": False,
                "explicacao": (
                    "As perdas caíram, mas entre uma ronda e outra a temperatura "
                    "continua subindo sem ninguém ver. E a anotação feita à mão "
                    "pode ter erro ou ser esquecida."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar sensores de temperatura sem fio com alerta no celular",
                "custo": 900,
                "perda_restante": 1500,
                "iot": True,
                "explicacao": (
                    "Os sensores mostraram que a temperatura sobe sempre entre 2h e 4h, "
                    "quando a equipe de carga deixa a porta aberta. Com o alerta, o "
                    "responsável fecha a porta em minutos e o problema real foi resolvido."
                ),
            },
            {
                "letra": "c",
                "texto": "Trocar a câmara fria inteira por um modelo novo",
                "custo": 12000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "Equipamento novo ajudou um pouco, mas a perda continuou: o "
                    "problema não era a máquina, era a porta aberta de madrugada. "
                    "Foi uma decisão cara tomada no achismo."
                ),
            },
        ],
        "conceito": {
            "titulo": "Monitoramento remoto com alerta por limite",
            "resumo": (
                "Sensores medem uma variável (aqui, a temperatura) o tempo todo e "
                "avisam automaticamente quando ela passa de um limite definido."
            ),
            "como_funciona": [
                "O sensor mede a temperatura a cada minuto.",
                "Um gateway recebe a leitura por rede sem fio e envia para a nuvem.",
                "Na nuvem existe um limite configurado (ex.: acima de -15 °C).",
                "Se o limite é ultrapassado, um alerta chega no celular do responsável.",
                "O histórico salvo mostra o padrão: em que horário o problema acontece.",
            ],
            "por_que_economiza": (
                "Você age no minuto em que o problema começa, e não horas depois. "
                "Além disso, o histórico revela a causa real, evitando gastar com a "
                "solução errada."
            ),
        },
    },
    {
        "numero": 2,
        "trilha": "industria",
        "ordem": 1,
        "setor": "Indústria 4.0",
        "titulo": "A máquina que para sem avisar",
        "problema": (
            "A principal prensa da sua fábrica quebra de surpresa cerca de duas "
            "vezes por mês. Cada parada deixa a linha de produção inteira "
            "esperando o conserto e atrasa entregas para clientes."
        ),
        "perda_atual": 20000,
        "vozes": [
            {
                "nome": "Roberto",
                "papel": "Chefe de manutenção",
                "fala": "Pra garantir, troco todas as peças todo mês. Melhor sobrar do que faltar.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Máquina costuma dar sinais antes de quebrar: vibra diferente, "
                    "esquenta mais. Se a gente medir isso, dá pra prever a falha."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Trocar as peças principais todo mês, mesmo que estejam boas",
                "custo": 9000,
                "perda_restante": 5000,
                "iot": False,
                "explicacao": (
                    "As quebras diminuíram, mas você jogou fora peças que ainda "
                    "durariam meses. E algumas falhas continuaram, porque vinham de "
                    "peças que não estavam na lista."
                ),
            },
            {
                "letra": "b",
                "texto": "Continuar como está: esperar quebrar e consertar",
                "custo": 0,
                "perda_restante": 20000,
                "iot": False,
                "explicacao": (
                    "Nada mudou. A fábrica continua refém de paradas inesperadas, "
                    "pagando por peças urgentes e por atrasos nas entregas."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar sensores de vibração e temperatura no motor da prensa",
                "custo": 1500,
                "perda_restante": 2000,
                "iot": True,
                "explicacao": (
                    "Os sensores avisaram com dias de antecedência quando um rolamento "
                    "começou a se desgastar. A troca foi agendada para o fim do turno, "
                    "sem parar a produção e sem trocar peça boa."
                ),
            },
        ],
        "conceito": {
            "titulo": "Manutenção preditiva",
            "resumo": (
                "Em vez de consertar depois que quebra (corretiva) ou trocar peças "
                "por calendário (preventiva), a IoT mede a saúde da máquina e prevê "
                "quando ela vai falhar."
            ),
            "como_funciona": [
                "Sensores de vibração e temperatura ficam presos ao motor.",
                "As leituras são enviadas continuamente para a nuvem.",
                "O sistema aprende qual é o comportamento normal da máquina.",
                "Quando a vibração foge do normal, gera um aviso de desgaste.",
                "A manutenção é agendada no melhor momento, antes da quebra.",
            ],
            "por_que_economiza": (
                "Você só troca o que realmente está gastando e evita paradas "
                "surpresa, que são a parte mais cara do problema."
            ),
        },
    },
    {
        "numero": 3,
        "trilha": "predial",
        "ordem": 2,
        "setor": "Utilities (água)",
        "titulo": "A conta de água que só cresce",
        "problema": (
            "A conta de água da empresa subiu muito nos últimos meses, sem "
            "aumento de produção ou de funcionários. Há suspeita de vazamento, "
            "mas a tubulação passa por dentro das paredes e do piso."
        ),
        "perda_atual": 7000,
        "vozes": [
            {
                "nome": "Carla",
                "papel": "Financeiro",
                "fala": "Acho que é desperdício do pessoal. Uma campanha de conscientização resolve.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Se medirmos o consumo por setor e por hora, um vazamento "
                    "aparece na hora: ele gasta água até de madrugada."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Instalar medidores inteligentes de água em cada setor",
                "custo": 700,
                "perda_restante": 800,
                "iot": True,
                "explicacao": (
                    "Na primeira noite, o medidor do galpão 2 mostrou consumo às 3h "
                    "da manhã, com tudo fechado. O vazamento foi localizado e "
                    "consertado sem quebrar paredes à toa."
                ),
            },
            {
                "letra": "b",
                "texto": "Fazer uma campanha pedindo para os funcionários economizarem",
                "custo": 0,
                "perda_restante": 6500,
                "iot": False,
                "explicacao": (
                    "Os funcionários colaboraram, mas a conta quase não mudou: o "
                    "problema era um vazamento, não comportamento. A suposição estava "
                    "errada e ninguém tinha dados para mostrar isso."
                ),
            },
            {
                "letra": "c",
                "texto": "Contratar uma empresa para inspecionar a tubulação a cada 3 meses",
                "custo": 2500,
                "perda_restante": 3500,
                "iot": False,
                "explicacao": (
                    "A inspeção achou o vazamento, mas só no fim do trimestre. Até "
                    "lá, a água continuou indo embora, e um novo vazamento pode "
                    "surgir logo depois da visita."
                ),
            },
        ],
        "conceito": {
            "titulo": "Telemetria de consumo e detecção de anomalias",
            "resumo": (
                "Medidores conectados enviam o consumo em tempo real, e o sistema "
                "identifica quando algo foge do padrão esperado."
            ),
            "como_funciona": [
                "Cada setor recebe um medidor de água com conexão à internet.",
                "O consumo é enviado para a nuvem várias vezes por hora.",
                "O sistema compara com o padrão normal (ex.: zero de madrugada).",
                "Consumo fora do padrão gera um alerta de possível vazamento.",
                "O painel mostra exatamente em qual setor está o problema.",
            ],
            "por_que_economiza": (
                "O vazamento é descoberto em horas, não em meses, e você sabe onde "
                "procurar. Isso também evita culpar as pessoas erradas."
            ),
        },
    },
    {
        "numero": 4,
        "trilha": "predial",
        "ordem": 1,
        "setor": "Edifícios inteligentes",
        "titulo": "Ar-condicionado ligado em salas vazias",
        "problema": (
            "A conta de energia do escritório está alta. Você percebeu que salas "
            "de reunião ficam com o ar-condicionado e as luzes ligados o dia "
            "inteiro, mesmo quando ninguém está usando."
        ),
        "perda_atual": 6000,
        "vozes": [
            {
                "nome": "Paulo",
                "papel": "Facilities",
                "fala": "Simples: desligo tudo no disjuntor às 18h e pronto.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "O desperdício acontece durante o dia, quando a sala fica vazia "
                    "entre reuniões. Precisamos saber se tem gente na sala."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Colar avisos de \"desligue ao sair\" em todas as salas",
                "custo": 100,
                "perda_restante": 4500,
                "iot": False,
                "explicacao": (
                    "Nas primeiras semanas funcionou um pouco, depois as pessoas se "
                    "acostumaram com os avisos e voltaram a esquecer."
                ),
            },
            {
                "letra": "b",
                "texto": "Desligar o ar-condicionado geral no disjuntor às 18h",
                "custo": 0,
                "perda_restante": 3500,
                "iot": False,
                "explicacao": (
                    "Economizou à noite, mas o desperdício durante o dia continuou. "
                    "E quem precisava trabalhar até mais tarde ficou sem ar."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar sensores de presença que ligam e desligam o ar sozinhos",
                "custo": 600,
                "perda_restante": 800,
                "iot": True,
                "explicacao": (
                    "Quando a sala fica 10 minutos vazia, o ar e as luzes desligam "
                    "sozinhos. Quando alguém entra, ligam de novo. Ninguém precisa "
                    "lembrar de nada."
                ),
            },
        ],
        "conceito": {
            "titulo": "Automação com sensores e atuadores",
            "resumo": (
                "IoT não serve só para medir: ela também pode agir. Um sensor "
                "detecta a situação e um atuador muda algo no ambiente "
                "automaticamente."
            ),
            "como_funciona": [
                "O sensor de presença detecta se há pessoas na sala.",
                "A informação vai para um controlador conectado à rede.",
                "Uma regra decide: \"sala vazia há 10 min → desligar\".",
                "O atuador (um relé inteligente) desliga o ar e as luzes.",
                "O painel mostra quanta energia foi economizada por sala.",
            ],
            "por_que_economiza": (
                "A economia não depende da memória das pessoas, acontece todo dia, "
                "em todas as salas, sem atrapalhar quem está trabalhando."
            ),
        },
    },
    {
        "numero": 5,
        "trilha": "agro",
        "ordem": 1,
        "setor": "Agronegócio",
        "titulo": "Irrigação no escuro",
        "problema": (
            "Na fazenda que fornece para sua empresa, a irrigação gasta muita "
            "água e energia com bombas. Mesmo assim, parte da plantação sofre "
            "ora com excesso, ora com falta de água."
        ),
        "perda_atual": 15000,
        "vozes": [
            {
                "nome": "Seu Antônio",
                "papel": "Gerente da fazenda",
                "fala": "Faço isso há 30 anos. Eu olho a terra e sei quando precisa molhar.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "A experiência do Seu Antônio é valiosa. Com sensores no solo, "
                    "ele passa a ter números pra confirmar o que sente."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Irrigar quando o gerente achar que o solo está seco",
                "custo": 0,
                "perda_restante": 9000,
                "iot": False,
                "explicacao": (
                    "Melhorou em relação ao horário fixo, mas a fazenda é grande e "
                    "ninguém consegue avaliar cada área todo dia. Algumas partes "
                    "continuaram secas e outras encharcadas."
                ),
            },
            {
                "letra": "b",
                "texto": "Usar sensores de umidade do solo junto com a previsão do tempo",
                "custo": 1800,
                "perda_restante": 3000,
                "iot": True,
                "explicacao": (
                    "Cada área só é irrigada quando o sensor indica solo seco e não "
                    "há chuva prevista. O consumo de água e energia caiu e a "
                    "produtividade subiu."
                ),
            },
            {
                "letra": "c",
                "texto": "Irrigar todos os dias no mesmo horário, chova ou faça sol",
                "custo": 0,
                "perda_restante": 15000,
                "iot": False,
                "explicacao": (
                    "Nada mudou: as bombas continuam ligando até em dia de chuva, e "
                    "a rotina fixa ignora que cada área do terreno tem uma "
                    "necessidade diferente."
                ),
            },
        ],
        "conceito": {
            "titulo": "Agricultura de precisão orientada por dados",
            "resumo": (
                "Sensores espalhados pelo campo mostram a real necessidade de cada "
                "área, e a decisão de irrigar passa a ser feita com base em dados."
            ),
            "como_funciona": [
                "Sensores enterrados medem a umidade do solo em cada área.",
                "As leituras viajam por rede de longo alcance (ex.: LoRaWAN) até a nuvem.",
                "O sistema cruza a umidade com a previsão do tempo.",
                "Só as áreas que precisam recebem água, no momento certo.",
                "O gerente acompanha tudo pelo celular e pode ajustar as regras.",
            ],
            "por_que_economiza": (
                "Água e energia são usadas só onde fazem diferença. A experiência "
                "do gerente continua importante, mas agora é confirmada por dados."
            ),
        },
    },
]


# ---------------------------------------------------------------------------
# Rodadas novas (Entrega 04): completam as 6 trilhas com 5 rodadas cada.
# Os cenários 1 a 5 acima foram distribuídos nas trilhas pelo campo "trilha".
# ---------------------------------------------------------------------------

CENARIOS += [
    # ======================= Trilha: Saúde e Cadeia Fria =======================
    {
        "numero": 6,
        "trilha": "saude",
        "ordem": 2,
        "setor": "Sala de vacinação",
        "titulo": "As vacinas que perdem a validade na geladeira",
        "problema": (
            "Na rede de clínicas, lotes de vacinas estão sendo descartados porque "
            "a geladeira saiu da faixa de 2 °C a 8 °C em algum momento. A "
            "funcionária anota a temperatura de manhã e à tarde, e nas duas "
            "anotações estava tudo certo."
        ),
        "perda_atual": 9000,
        "vozes": [
            {
                "nome": "Dra. Helena",
                "papel": "Coordenadora das clínicas",
                "fala": "Essa geladeira já deu o que tinha que dar. Vamos comprar uma nova e pronto.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Duas anotações por dia não mostram o que acontece de noite ou "
                    "no fim de semana. Precisamos de um registro contínuo."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Pedir para anotar a temperatura de hora em hora durante o expediente",
                "custo": 300,
                "perda_restante": 5000,
                "iot": False,
                "explicacao": (
                    "As anotações aumentaram, mas o problema acontecia de madrugada, "
                    "quando a clínica está fechada. Ninguém estava lá para ver."
                ),
            },
            {
                "letra": "b",
                "texto": "Comprar uma geladeira científica nova para cada clínica",
                "custo": 3500,
                "perda_restante": 2500,
                "iot": False,
                "explicacao": (
                    "A geladeira nova é melhor, mas quedas de energia à noite "
                    "continuaram estragando lotes. E ninguém era avisado a tempo."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar registradores de temperatura conectados com alerta no celular",
                "custo": 500,
                "perda_restante": 600,
                "iot": True,
                "explicacao": (
                    "O registrador mostrou que a energia caía em algumas madrugadas. "
                    "Com o alerta, o plantonista leva as vacinas para a caixa térmica "
                    "na hora. E o relatório de temperatura sai pronto para a vigilância sanitária."
                ),
            },
        ],
        "conceito": {
            "titulo": "Registro contínuo de temperatura (data logger conectado)",
            "resumo": (
                "Um sensor guarda a temperatura minuto a minuto, 24 horas por dia, "
                "e manda o histórico para a nuvem. Nada fica sem registro."
            ),
            "como_funciona": [
                "O registrador fica dentro da geladeira e mede a temperatura a cada minuto.",
                "As leituras vão pela internet (Wi-Fi ou chip de celular) para a nuvem.",
                "Se sair da faixa de 2 °C a 8 °C, o responsável recebe um alerta.",
                "O sistema gera sozinho o relatório exigido pela vigilância sanitária.",
            ],
            "por_que_economiza": (
                "Você descobre o problema na hora em que ele começa, inclusive de "
                "madrugada, e salva o lote antes que ele estrague."
            ),
        },
    },
    {
        "numero": 7,
        "trilha": "saude",
        "ordem": 4,
        "setor": "Hospital",
        "titulo": "As bombas de infusão que ninguém encontra",
        "problema": (
            "A enfermagem do hospital perde muito tempo procurando bombas de "
            "infusão e cadeiras de rodas. Como ninguém acha, o hospital acaba "
            "alugando equipamentos extras, mesmo tendo vários parados em algum "
            "corredor ou depósito."
        ),
        "perda_atual": 16000,
        "vozes": [
            {
                "nome": "Sônia",
                "papel": "Chefe de enfermagem",
                "fala": "Faltam equipamentos. Precisamos alugar pelo menos mais vinte bombas.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Será que faltam mesmo, ou só não sabemos onde estão? Se cada "
                    "equipamento mostrasse onde está, a resposta ficaria clara."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Alugar mais 20 bombas de infusão",
                "custo": 8000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "A falta diminuiu, mas os equipamentos novos também começaram a "
                    "sumir pelos andares. O hospital passou a pagar por mais "
                    "aparelhos sem resolver a causa."
                ),
            },
            {
                "letra": "b",
                "texto": "Colocar etiquetas de localização nos equipamentos, com mapa no computador",
                "custo": 1800,
                "perda_restante": 2000,
                "iot": True,
                "explicacao": (
                    "Em segundos a enfermeira vê no mapa onde está a bomba livre mais "
                    "próxima. Descobriu-se que 30% delas ficavam esquecidas no "
                    "depósito. O aluguel extra foi cancelado."
                ),
            },
            {
                "letra": "c",
                "texto": "Fazer um inventário manual de todos os equipamentos toda semana",
                "custo": 2500,
                "perda_restante": 11000,
                "iot": False,
                "explicacao": (
                    "O inventário mostra onde as coisas estavam na segunda-feira. Na "
                    "terça, tudo já mudou de lugar de novo. A procura continuou."
                ),
            },
        ],
        "conceito": {
            "titulo": "Rastreamento de ativos em tempo real",
            "resumo": (
                "Pequenas etiquetas sem fio presas aos equipamentos avisam onde eles "
                "estão a todo momento, como um GPS para dentro do prédio."
            ),
            "como_funciona": [
                "Cada equipamento recebe uma etiqueta Bluetooth do tamanho de uma moeda.",
                "Receptores espalhados pelos andares captam o sinal das etiquetas.",
                "O sistema calcula em qual sala cada equipamento está.",
                "A equipe consulta tudo num mapa, no computador ou no celular.",
            ],
            "por_que_economiza": (
                "Você usa melhor o que já tem antes de comprar ou alugar mais, e a "
                "equipe para de perder tempo procurando."
            ),
        },
    },
    {
        "numero": 8,
        "trilha": "saude",
        "ordem": 3,
        "setor": "Transporte de medicamentos",
        "titulo": "Cargas de remédio recusadas na entrega",
        "problema": (
            "Sua distribuidora leva medicamentos refrigerados para hospitais. "
            "Algumas cargas chegam fora da temperatura e o hospital recusa tudo. "
            "Você só descobre o problema quando o caminhão já chegou."
        ),
        "perda_atual": 14000,
        "vozes": [
            {
                "nome": "Jorge",
                "papel": "Coordenador de frota",
                "fala": "É só colocar mais gelo nas caixas. Sempre funcionou assim.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "A carga passa horas na estrada sem ninguém saber como está. Se "
                    "a temperatura começa a subir, dá tempo de agir antes de chegar."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Colocar sensores de temperatura e GPS no baú, com acompanhamento ao vivo",
                "custo": 1200,
                "perda_restante": 2000,
                "iot": True,
                "explicacao": (
                    "Numa viagem, o alerta mostrou que o refrigerador do baú falhou. "
                    "O motorista parou numa base de apoio e trocou a carga de "
                    "caminhão a tempo. O hospital recebeu tudo certinho."
                ),
            },
            {
                "letra": "b",
                "texto": "Reforçar as caixas com mais gelo e isopor mais grosso",
                "custo": 2000,
                "perda_restante": 8000,
                "iot": False,
                "explicacao": (
                    "Ajudou nas viagens curtas, mas nas longas o gelo não segurou. "
                    "E em algumas cargas o excesso de gelo deixou o remédio frio "
                    "demais, o que também é proibido."
                ),
            },
            {
                "letra": "c",
                "texto": "Trocar para uma transportadora mais cara e mais conhecida",
                "custo": 6000,
                "perda_restante": 5000,
                "iot": False,
                "explicacao": (
                    "As recusas caíram, mas o custo subiu muito. E quando acontece "
                    "um problema, você continua sem saber onde nem quando."
                ),
            },
        ],
        "conceito": {
            "titulo": "Rastreamento de carga com monitoramento de condição",
            "resumo": (
                "O baú do caminhão envia, durante toda a viagem, onde está e em que "
                "temperatura está a carga."
            ),
            "como_funciona": [
                "Um sensor de temperatura e um GPS ficam dentro do baú.",
                "Um chip de celular envia as leituras para a nuvem a cada poucos minutos.",
                "A central acompanha todas as cargas num mapa.",
                "Se a temperatura sai da faixa, motorista e central recebem um alerta.",
            ],
            "por_que_economiza": (
                "O problema é resolvido no caminho, e não descoberto na porta do "
                "cliente. Você também prova que a carga viajou do jeito certo."
            ),
        },
    },
    {
        "numero": 9,
        "trilha": "saude",
        "ordem": 5,
        "setor": "Clínica",
        "titulo": "O oxigênio que acaba de surpresa",
        "problema": (
            "Na clínica, os cilindros de oxigênio às vezes acabam antes do "
            "previsto. Aí é preciso fazer um pedido de emergência, com frete "
            "urgente e muito mais caro, e a equipe fica sob pressão."
        ),
        "perda_atual": 10000,
        "vozes": [
            {
                "nome": "Fernanda",
                "papel": "Compras",
                "fala": "Vamos manter o dobro de cilindros no estoque. Assim nunca falta.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Estoque dobrado custa caro e ocupa espaço. Se a gente souber o "
                    "nível de cada cilindro, dá pra pedir na hora certa."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Manter o dobro de cilindros cheios no estoque",
                "custo": 3000,
                "perda_restante": 4000,
                "iot": False,
                "explicacao": (
                    "As emergências diminuíram, mas você passou a pagar aluguel de "
                    "cilindros parados. E quando o consumo aumenta de repente, ainda falta."
                ),
            },
            {
                "letra": "b",
                "texto": "Pedir para a equipe olhar os manômetros a cada troca de turno",
                "custo": 1500,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "Em dias corridos a conferência é esquecida, e entre um turno e "
                    "outro o consumo pode disparar. As compras de urgência continuaram."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar sensores de pressão nos cilindros com pedido automático ao fornecedor",
                "custo": 900,
                "perda_restante": 1200,
                "iot": True,
                "explicacao": (
                    "Quando um cilindro chega a 30%, o fornecedor já recebe o pedido "
                    "automaticamente. A reposição chega no prazo normal, sem frete "
                    "urgente e sem estoque sobrando."
                ),
            },
        ],
        "conceito": {
            "titulo": "Monitoramento de nível com reposição automática",
            "resumo": (
                "Sensores medem quanto ainda resta de um insumo e disparam o pedido "
                "de reposição sozinhos, no momento certo."
            ),
            "como_funciona": [
                "Um sensor de pressão é instalado na saída de cada cilindro.",
                "A pressão é convertida em porcentagem de oxigênio restante.",
                "O painel mostra todos os cilindros e quanto tempo cada um ainda dura.",
                "Ao chegar no nível mínimo, o pedido vai direto para o fornecedor.",
            ],
            "por_que_economiza": (
                "Acabam as compras de emergência e o estoque fica do tamanho certo: "
                "nem falta, nem sobra parado."
            ),
        },
    },

    # ======================= Trilha: Indústria e Manufatura =======================
    {
        "numero": 10,
        "trilha": "industria",
        "ordem": 3,
        "setor": "Ar comprimido",
        "titulo": "O compressor que não descansa",
        "problema": (
            "O compressor de ar da fábrica fica ligado o tempo todo, inclusive no "
            "almoço e à noite, e a conta de energia não para de subir. A "
            "produção não aumentou, mas o compressor parece não dar conta."
        ),
        "perda_atual": 9000,
        "vozes": [
            {
                "nome": "Valter",
                "papel": "Supervisor de produção",
                "fala": "Esse compressor é pequeno pra fábrica. Tem que comprar um maior.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Se ele trabalha até com a fábrica parada, o ar está escapando "
                    "por algum lugar. Vazamento de ar não faz barulho, mas custa caro."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Comprar um compressor maior e mais potente",
                "custo": 5000,
                "perda_restante": 7000,
                "iot": False,
                "explicacao": (
                    "O compressor novo enche mais rápido, mas o ar continua escapando "
                    "pelos mesmos vazamentos. Agora você paga a parcela da máquina e "
                    "uma conta de luz quase igual."
                ),
            },
            {
                "letra": "b",
                "texto": "Pedir para o último a sair desligar o compressor no almoço e à noite",
                "custo": 0,
                "perda_restante": 7500,
                "iot": False,
                "explicacao": (
                    "Nos dias em que alguém lembrou, economizou um pouco. Mas os "
                    "vazamentos continuam durante todo o expediente, que é quando "
                    "o desperdício é maior."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar medidores de energia e de pressão na rede de ar comprimido",
                "custo": 800,
                "perda_restante": 2000,
                "iot": True,
                "explicacao": (
                    "Com a fábrica parada, a pressão caía rápido: prova de vazamento. "
                    "Os medidores por setor mostraram onde estavam as mangueiras "
                    "furadas. Consertadas, o compressor passou a descansar."
                ),
            },
        ],
        "conceito": {
            "titulo": "Medição de energia e detecção de vazamentos",
            "resumo": (
                "Medir o consumo e a pressão ao longo do dia mostra o que é uso de "
                "verdade e o que é desperdício escondido."
            ),
            "como_funciona": [
                "Um medidor registra quanta energia o compressor gasta a cada minuto.",
                "Sensores de pressão ficam em pontos diferentes da rede de ar.",
                "O sistema compara o consumo com a fábrica funcionando e parada.",
                "Queda de pressão sem produção indica vazamento, e o setor aparece no painel.",
            ],
            "por_que_economiza": (
                "Você conserta a causa (o vazamento) em vez de comprar uma máquina "
                "maior, e passa a ver o resultado na conta de luz."
            ),
        },
    },
    {
        "numero": 11,
        "trilha": "industria",
        "ordem": 2,
        "setor": "Injeção plástica",
        "titulo": "O lote com defeito descoberto tarde demais",
        "problema": (
            "As injetoras de plástico fazem milhares de peças por dia. De vez em "
            "quando, um lote inteiro sai com defeito, e isso só é percebido na "
            "inspeção do fim do dia. Aí tudo vai para o lixo."
        ),
        "perda_atual": 18000,
        "vozes": [
            {
                "nome": "Cláudia",
                "papel": "Gerente de qualidade",
                "fala": "Precisamos inspecionar mais peças. Mais gente olhando, menos defeito.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Inspecionar mais só descobre o defeito mais cedo. O ideal é "
                    "perceber quando a máquina começa a sair do ponto, antes de "
                    "fazer peça ruim."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Inspecionar uma peça a cada 20, em vez de uma a cada 100",
                "custo": 2500,
                "perda_restante": 11000,
                "iot": False,
                "explicacao": (
                    "O defeito passou a ser achado um pouco antes, mas várias "
                    "centenas de peças ruins já tinham sido feitas. E o custo com "
                    "inspetores aumentou."
                ),
            },
            {
                "letra": "b",
                "texto": "Inspecionar 100% das peças no fim da linha",
                "custo": 7000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "Nenhuma peça ruim chega ao cliente, mas a fábrica continua "
                    "fabricando e jogando fora peças com defeito. Só mudou o lugar "
                    "onde o prejuízo aparece."
                ),
            },
            {
                "letra": "c",
                "texto": "Colocar sensores de temperatura e pressão nas injetoras, com parada automática",
                "custo": 2000,
                "perda_restante": 2500,
                "iot": True,
                "explicacao": (
                    "Os sensores mostraram que o molde esquentava demais depois de "
                    "algumas horas. Agora, quando sai do ponto, a máquina avisa e "
                    "para antes de fazer peça ruim."
                ),
            },
        ],
        "conceito": {
            "titulo": "Controle de qualidade em tempo real",
            "resumo": (
                "Em vez de procurar o defeito na peça pronta, os sensores vigiam o "
                "processo e avisam quando ele começa a sair do padrão."
            ),
            "como_funciona": [
                "Sensores medem temperatura do molde e pressão de injeção a cada ciclo.",
                "O sistema conhece a faixa em que a peça sai boa.",
                "Se a medida sai da faixa, o operador recebe um aviso na máquina.",
                "Se a variação continua, a injetora para sozinha antes do lote se perder.",
            ],
            "por_que_economiza": (
                "Você evita fabricar o defeito, e não só encontrá-lo. Menos material "
                "no lixo e menos horas de máquina desperdiçadas."
            ),
        },
    },
    {
        "numero": 12,
        "trilha": "industria",
        "ordem": 5,
        "setor": "Gestão da produção",
        "titulo": "Ninguém sabe quanto a fábrica produz de verdade",
        "problema": (
            "A meta de produção quase nunca é batida. Os operadores anotam as "
            "paradas num papel, mas pequenas paradas não são registradas, e "
            "ninguém sabe onde o tempo está sendo perdido."
        ),
        "perda_atual": 15000,
        "vozes": [
            {
                "nome": "Sr. Carlos",
                "papel": "Diretor industrial",
                "fala": "Se a meta não sai, vamos fazer hora extra até sair.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Antes de trabalhar mais, vale descobrir para onde está indo o "
                    "tempo. Muitas paradas pequenas viram horas perdidas no fim do mês."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Fazer hora extra todos os sábados para bater a meta",
                "custo": 5000,
                "perda_restante": 12000,
                "iot": False,
                "explicacao": (
                    "A produção do mês melhorou um pouco, mas a um custo alto e com "
                    "a equipe cansada. As mesmas paradas continuaram acontecendo "
                    "durante a semana."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar sensores que contam peças e registram cada parada das máquinas",
                "custo": 1500,
                "perda_restante": 4000,
                "iot": True,
                "explicacao": (
                    "O painel mostrou que a troca de ferramenta levava 40 minutos e "
                    "acontecia várias vezes por dia. Com um ajuste no processo, a "
                    "fábrica ganhou quase um turno por semana sem hora extra."
                ),
            },
            {
                "letra": "c",
                "texto": "Contratar uma pessoa para anotar a produção em cada linha",
                "custo": 6000,
                "perda_restante": 9000,
                "iot": False,
                "explicacao": (
                    "Os dados melhoraram, mas chegam atrasados e com erros de "
                    "digitação. As paradas curtas ainda passam despercebidas."
                ),
            },
        ],
        "conceito": {
            "titulo": "Monitoramento de produção e OEE",
            "resumo": (
                "Sensores simples nas máquinas contam a produção e registram cada "
                "parada, mostrando a eficiência real da fábrica (o chamado OEE)."
            ),
            "como_funciona": [
                "Um sensor detecta cada peça produzida e se a máquina está parada ou rodando.",
                "Os dados vão automaticamente para um painel, sem anotação em papel.",
                "O sistema calcula a eficiência de cada máquina e de cada turno.",
                "O gráfico de paradas mostra quais motivos mais roubam tempo.",
            ],
            "por_que_economiza": (
                "Você ataca as perdas maiores primeiro e ganha produção com as "
                "mesmas máquinas e a mesma equipe."
            ),
        },
    },
    {
        "numero": 13,
        "trilha": "industria",
        "ordem": 4,
        "setor": "Energia",
        "titulo": "A multa de energia que chega todo mês",
        "problema": (
            "A fábrica tem um limite de potência contratado com a distribuidora de "
            "energia. Quando várias máquinas grandes ligam juntas, esse limite é "
            "ultrapassado e a conta vem com multa."
        ),
        "perda_atual": 12000,
        "vozes": [
            {
                "nome": "Rita",
                "papel": "Financeiro",
                "fala": "Melhor aumentar o contrato com a distribuidora e parar de pagar multa.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Os picos duram poucos minutos. Se a gente enxergar o consumo em "
                    "tempo real, dá pra evitar que as máquinas grandes liguem juntas."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Escrever uma regra proibindo ligar as máquinas grandes ao mesmo tempo",
                "custo": 0,
                "perda_restante": 7000,
                "iot": False,
                "explicacao": (
                    "Ajudou nos primeiros dias. Mas, com pressa, os operadores não "
                    "sabem o que as outras áreas estão ligando, e as multas voltaram."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar um medidor inteligente que avisa antes de estourar o limite",
                "custo": 1000,
                "perda_restante": 1500,
                "iot": True,
                "explicacao": (
                    "Quando o consumo chega a 90% do limite, o sistema avisa e "
                    "segura por alguns minutos o ligamento de cargas não urgentes. "
                    "As multas praticamente sumiram."
                ),
            },
            {
                "letra": "c",
                "texto": "Aumentar a potência contratada com a distribuidora",
                "custo": 4500,
                "perda_restante": 3000,
                "iot": False,
                "explicacao": (
                    "As multas diminuíram, mas agora você paga por uma potência "
                    "maior o mês inteiro, mesmo usando ela só alguns minutos por dia."
                ),
            },
        ],
        "conceito": {
            "titulo": "Gestão de demanda de energia",
            "resumo": (
                "Um medidor conectado acompanha a potência usada pela fábrica a cada "
                "instante e ajuda a evitar picos que geram multa."
            ),
            "como_funciona": [
                "O medidor inteligente fica na entrada de energia da fábrica.",
                "Ele envia a potência consumida a cada minuto para o sistema.",
                "Perto do limite contratado, o sistema dispara um alerta.",
                "Cargas que podem esperar (como aquecedores) são adiadas por alguns minutos.",
            ],
            "por_que_economiza": (
                "Você para de pagar multa sem precisar contratar mais energia do que "
                "realmente usa."
            ),
        },
    },

    # ======================= Trilha: Logística e Varejo =======================
    {
        "numero": 14,
        "trilha": "logistica",
        "ordem": 1,
        "setor": "Frota de caminhões",
        "titulo": "O combustível que some na estrada",
        "problema": (
            "O gasto com diesel da frota cresce todo mês. Os caminhões rodam mais "
            "quilômetros do que o planejado e muitos ficam parados com o motor "
            "ligado. Você não sabe o que acontece depois que eles saem do pátio."
        ),
        "perda_atual": 20000,
        "vozes": [
            {
                "nome": "Edson",
                "papel": "Gerente de frota",
                "fala": "Caminhão velho bebe muito. Tem que renovar a frota.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Antes de trocar caminhão, vamos ver como eles estão sendo "
                    "usados: rota, velocidade, tempo de motor ligado parado."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Pedir que cada motorista entregue um relatório em papel no fim do dia",
                "custo": 300,
                "perda_restante": 17000,
                "iot": False,
                "explicacao": (
                    "Os relatórios chegam incompletos e é impossível conferir. O "
                    "consumo quase não mudou."
                ),
            },
            {
                "letra": "b",
                "texto": "Trocar a frota por caminhões novos e mais econômicos",
                "custo": 15000,
                "perda_restante": 10000,
                "iot": False,
                "explicacao": (
                    "Os caminhões novos gastam menos, mas a parcela é altíssima. E "
                    "os desvios de rota e o motor ligado parado continuaram."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar rastreadores com telemetria: rota, velocidade e consumo",
                "custo": 2500,
                "perda_restante": 6000,
                "iot": True,
                "explicacao": (
                    "O painel mostrou caminhões parados com motor ligado por horas e "
                    "rotas mais longas que o necessário. Com rotas melhores e "
                    "orientação aos motoristas, o diesel caiu bastante."
                ),
            },
        ],
        "conceito": {
            "titulo": "Telemetria veicular",
            "resumo": (
                "Um equipamento no caminhão envia, em tempo real, onde ele está e "
                "como está sendo dirigido."
            ),
            "como_funciona": [
                "O rastreador é ligado ao GPS e ao computador de bordo do caminhão.",
                "Posição, velocidade, consumo e tempo de motor ligado vão para a nuvem.",
                "O sistema compara a rota feita com a rota planejada.",
                "Relatórios mostram desperdícios por caminhão e por motorista.",
            ],
            "por_que_economiza": (
                "Você corta o desperdício de diesel na causa (rota e forma de "
                "dirigir) sem precisar trocar a frota."
            ),
        },
    },
    {
        "numero": 15,
        "trilha": "logistica",
        "ordem": 4,
        "setor": "Supermercado",
        "titulo": "A prateleira vazia na hora do movimento",
        "problema": (
            "Nos horários de pico, produtos que vendem muito somem das "
            "prateleiras, mesmo tendo estoque no depósito. O cliente não encontra "
            "e vai embora ou compra no concorrente."
        ),
        "perda_atual": 16000,
        "vozes": [
            {
                "nome": "Luciana",
                "papel": "Gerente da loja",
                "fala": "Faltam repositores. Vou contratar mais gente para os corredores.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "O problema não é falta de produto, é o momento da reposição. "
                    "Se a prateleira avisasse que está esvaziando, a equipe chegaria a tempo."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Contratar mais repositores para todos os turnos",
                "custo": 6000,
                "perda_restante": 7000,
                "iot": False,
                "explicacao": (
                    "As prateleiras ficaram mais cheias, mas os repositores passavam "
                    "boa parte do tempo sem saber qual corredor precisava deles."
                ),
            },
            {
                "letra": "b",
                "texto": "Colocar sensores de peso nas prateleiras com aviso de reposição",
                "custo": 2000,
                "perda_restante": 3000,
                "iot": True,
                "explicacao": (
                    "Quando a prateleira chega a 20%, o repositor recebe um aviso no "
                    "celular com o corredor e o produto. A equipe atual passou a dar conta."
                ),
            },
            {
                "letra": "c",
                "texto": "Pedir mais mercadoria ao fornecedor para nunca faltar",
                "custo": 4000,
                "perda_restante": 9000,
                "iot": False,
                "explicacao": (
                    "O depósito ficou lotado e o capital ficou parado em estoque. Mas "
                    "a prateleira continuou vazia, porque o problema era a reposição."
                ),
            },
        ],
        "conceito": {
            "titulo": "Prateleira inteligente",
            "resumo": (
                "Sensores na prateleira medem quanto produto ainda está exposto e "
                "avisam a equipe na hora de repor."
            ),
            "como_funciona": [
                "Balanças finas ficam embaixo dos produtos de maior giro.",
                "O peso é convertido em quantidade de itens na prateleira.",
                "Abaixo do mínimo, o sistema avisa o repositor com o corredor exato.",
                "O histórico mostra os horários em que cada produto mais vende.",
            ],
            "por_que_economiza": (
                "Você não perde venda por falta de produto exposto e usa melhor o "
                "tempo da equipe que já tem."
            ),
        },
    },
    {
        "numero": 16,
        "trilha": "logistica",
        "ordem": 2,
        "setor": "Centro de distribuição",
        "titulo": "Os paletes perdidos no armazém",
        "problema": (
            "No centro de distribuição, mercadorias são guardadas no lugar errado "
            "e ninguém encontra. Pedidos atrasam, separadores perdem tempo "
            "procurando e às vezes compra-se de novo algo que já estava no estoque."
        ),
        "perda_atual": 13000,
        "vozes": [
            {
                "nome": "Marcos",
                "papel": "Supervisor do armazém",
                "fala": "Precisamos de mais separadores. Do jeito que está, não dá conta.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Se cada palete dissesse onde está e por onde passou, a busca "
                    "acabaria. O problema é informação, não braço."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Colocar etiquetas RFID nos paletes e leitores nas portas e corredores",
                "custo": 2200,
                "perda_restante": 2500,
                "iot": True,
                "explicacao": (
                    "Cada palete é registrado automaticamente ao passar pelos "
                    "leitores. O sistema mostra a posição de qualquer item em "
                    "segundos, e os atrasos caíram muito."
                ),
            },
            {
                "letra": "b",
                "texto": "Fazer um inventário geral do armazém todo mês",
                "custo": 3000,
                "perda_restante": 8000,
                "iot": False,
                "explicacao": (
                    "O inventário arruma tudo por alguns dias, mas logo os paletes "
                    "voltam a ser guardados em lugares errados e a confusão volta."
                ),
            },
            {
                "letra": "c",
                "texto": "Contratar mais separadores para compensar o tempo de busca",
                "custo": 5000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "Os pedidos saíram mais rápido, mas agora mais gente perde tempo "
                    "procurando. O custo subiu e a causa continuou a mesma."
                ),
            },
        ],
        "conceito": {
            "titulo": "Identificação por radiofrequência (RFID)",
            "resumo": (
                "Etiquetas que não precisam de bateria são lidas à distância por "
                "antenas, registrando a passagem dos produtos sem ninguém digitar nada."
            ),
            "como_funciona": [
                "Cada palete recebe uma etiqueta RFID com um código único.",
                "Antenas nas portas e corredores leem as etiquetas que passam por perto.",
                "O sistema registra onde e quando cada palete foi visto pela última vez.",
                "O separador pesquisa o produto e vê a localização no celular.",
            ],
            "por_que_economiza": (
                "Acaba o tempo de procura e as compras repetidas, e o estoque do "
                "sistema passa a bater com o estoque real."
            ),
        },
    },
    {
        "numero": 17,
        "trilha": "logistica",
        "ordem": 3,
        "setor": "Entregas",
        "titulo": "O telefone que não para: \"Cadê meu pedido?\"",
        "problema": (
            "A central de atendimento da sua loja online vive lotada de clientes "
            "perguntando onde está a entrega. Os atendentes também não sabem, "
            "precisam ligar para o motorista, e o cliente fica irritado."
        ),
        "perda_atual": 9000,
        "vozes": [
            {
                "nome": "Patrícia",
                "papel": "Atendimento ao cliente",
                "fala": "Preciso de mais dois atendentes, a fila de ligações não acaba.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Se o cliente pudesse ver sozinho onde está a entrega, metade "
                    "dessas ligações nem existiria."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Contratar mais dois atendentes",
                "custo": 5000,
                "perda_restante": 4000,
                "iot": False,
                "explicacao": (
                    "A fila diminuiu, mas os atendentes continuam sem a informação. "
                    "Cada ligação ainda é demorada e o cliente segue sem previsão certa."
                ),
            },
            {
                "letra": "b",
                "texto": "Dar cupom de desconto para quem reclamar do atraso",
                "custo": 3000,
                "perda_restante": 7000,
                "iot": False,
                "explicacao": (
                    "Alguns clientes ficaram satisfeitos, mas as ligações "
                    "continuaram, e o cupom virou mais um custo todo mês."
                ),
            },
            {
                "letra": "c",
                "texto": "Rastrear os veículos e enviar ao cliente um link para acompanhar a entrega",
                "custo": 900,
                "perda_restante": 1500,
                "iot": True,
                "explicacao": (
                    "O cliente recebe uma mensagem com o link e vê o carro chegando "
                    "no mapa, com horário previsto. As ligações caíram mais da metade."
                ),
            },
        ],
        "conceito": {
            "titulo": "Rastreamento de entregas em tempo real",
            "resumo": (
                "A posição de cada veículo é compartilhada com quem precisa dela: a "
                "central e o próprio cliente."
            ),
            "como_funciona": [
                "Um rastreador GPS ou o celular do motorista envia a posição a cada minuto.",
                "O sistema calcula o horário previsto de chegada de cada entrega.",
                "O cliente recebe um link por mensagem para acompanhar no mapa.",
                "Atrasos geram aviso automático antes de o cliente precisar ligar.",
            ],
            "por_que_economiza": (
                "Você reduz o volume do atendimento e melhora a experiência do "
                "cliente ao mesmo tempo."
            ),
        },
    },
    {
        "numero": 18,
        "trilha": "logistica",
        "ordem": 5,
        "setor": "Loja de varejo",
        "titulo": "A fila no caixa na hora errada",
        "problema": (
            "Em alguns horários a loja fica cheia, a fila no caixa cresce e "
            "clientes desistem da compra. Em outros, funcionários ficam parados. "
            "A escala é sempre a mesma, todos os dias."
        ),
        "perda_atual": 11000,
        "vozes": [
            {
                "nome": "Renato",
                "papel": "Gerente regional",
                "fala": "Coloca mais gente em todos os turnos. Fila é cliente perdido.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "O movimento muda conforme o dia e a hora. Se contarmos quem "
                    "entra na loja, a escala pode acompanhar o movimento real."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Manter a escala e abrir um caixa extra quando o gerente perceber a fila",
                "custo": 0,
                "perda_restante": 8000,
                "iot": False,
                "explicacao": (
                    "Quando o gerente percebe, a fila já está grande e muitos "
                    "clientes já foram embora. A reação vem sempre atrasada."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar contadores de pessoas na entrada e montar a escala pelos dados",
                "custo": 900,
                "perda_restante": 2500,
                "iot": True,
                "explicacao": (
                    "Os dados mostraram picos às sextas no fim da tarde e no sábado "
                    "de manhã. A escala foi ajustada sem contratar ninguém, e as "
                    "desistências caíram."
                ),
            },
            {
                "letra": "c",
                "texto": "Contratar mais funcionários para todos os turnos",
                "custo": 7000,
                "perda_restante": 3500,
                "iot": False,
                "explicacao": (
                    "As filas diminuíram, mas nos horários vazios a loja ficou cheia "
                    "de funcionários parados. O custo engoliu quase todo o ganho."
                ),
            },
        ],
        "conceito": {
            "titulo": "Contagem de fluxo de pessoas",
            "resumo": (
                "Sensores na porta contam quantas pessoas entram e saem, mostrando o "
                "movimento real da loja hora a hora."
            ),
            "como_funciona": [
                "Um sensor no teto da entrada conta as pessoas que passam (sem filmar rostos).",
                "As contagens vão para um painel com o movimento por hora e dia da semana.",
                "O sistema compara o movimento com o número de caixas abertos.",
                "A escala da semana seguinte é montada a partir desses números.",
            ],
            "por_que_economiza": (
                "Você coloca as pessoas certas na hora certa: menos fila no pico e "
                "menos gente parada no horário vazio."
            ),
        },
    },

    # ======================= Trilha: Infraestrutura Predial =======================
    {
        "numero": 19,
        "trilha": "predial",
        "ordem": 4,
        "setor": "Elevadores",
        "titulo": "O elevador que vive parado",
        "problema": (
            "No prédio comercial que você administra, os elevadores param com "
            "frequência. Os inquilinos reclamam, e a empresa de manutenção só "
            "aparece depois do chamado, às vezes no dia seguinte."
        ),
        "perda_atual": 8000,
        "vozes": [
            {
                "nome": "Dona Célia",
                "papel": "Síndica",
                "fala": "Vou exigir que a empresa de manutenção venha toda semana.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Visitar toda semana não garante achar o defeito. O elevador dá "
                    "sinais antes de parar: porta demorando, motor esquentando."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Instalar sensores no elevador que avisam sinais de falha",
                "custo": 800,
                "perda_restante": 1500,
                "iot": True,
                "explicacao": (
                    "O sistema avisou que a porta do elevador 2 estava demorando "
                    "cada vez mais para fechar. O técnico trocou a peça antes de "
                    "travar, e as paradas caíram muito."
                ),
            },
            {
                "letra": "b",
                "texto": "Pagar visitas semanais da empresa de manutenção",
                "custo": 3500,
                "perda_restante": 4000,
                "iot": False,
                "explicacao": (
                    "As visitas ajudaram, mas o técnico olha o elevador por pouco "
                    "tempo e nem sempre pega o problema. E o contrato ficou bem mais caro."
                ),
            },
            {
                "letra": "c",
                "texto": "Manter como está e chamar o técnico quando o elevador parar",
                "custo": 0,
                "perda_restante": 8000,
                "iot": False,
                "explicacao": (
                    "Nada mudou: os inquilinos continuam presos ou subindo escada, e "
                    "cada chamado de emergência sai caro."
                ),
            },
        ],
        "conceito": {
            "titulo": "Manutenção preditiva de equipamentos prediais",
            "resumo": (
                "Sensores acompanham o funcionamento do equipamento e avisam quando "
                "ele começa a se comportar diferente do normal."
            ),
            "como_funciona": [
                "Sensores registram viagens, tempo de abertura de porta e temperatura do motor.",
                "Os dados são enviados para a nuvem pela internet do prédio.",
                "O sistema aprende o comportamento normal de cada elevador.",
                "Sinais de desgaste geram um chamado antes da parada.",
            ],
            "por_que_economiza": (
                "Os reparos são feitos de forma planejada e mais barata, e o "
                "elevador quase não para."
            ),
        },
    },
    {
        "numero": 20,
        "trilha": "predial",
        "ordem": 3,
        "setor": "Bombas e reservatórios",
        "titulo": "A caixa d'água que transborda de madrugada",
        "problema": (
            "No condomínio, a caixa d'água às vezes transborda de madrugada e, em "
            "outros dias, fica vazia de manhã. A bomba já queimou duas vezes "
            "neste ano por trabalhar sem água."
        ),
        "perda_atual": 6000,
        "vozes": [
            {
                "nome": "Seu Raimundo",
                "papel": "Zelador",
                "fala": "Deixa comigo: eu ligo e desligo a bomba na mão, como antigamente.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "O Seu Raimundo não pode ficar acordado a noite toda. Um sensor "
                    "de nível faz esse trabalho sem descanso."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Trocar a boia da caixa d'água a cada seis meses",
                "custo": 300,
                "perda_restante": 3000,
                "iot": False,
                "explicacao": (
                    "Boia nova ajuda por um tempo, mas ninguém fica sabendo quando "
                    "ela trava. Os transbordos e a bomba seca continuaram de vez em quando."
                ),
            },
            {
                "letra": "b",
                "texto": "Colocar o zelador para ligar e desligar a bomba manualmente",
                "custo": 1200,
                "perda_restante": 2500,
                "iot": False,
                "explicacao": (
                    "Funcionou durante o dia, mas à noite e nos fins de semana "
                    "ninguém estava lá. E o condomínio passou a pagar hora extra."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar sensor de nível com controle automático da bomba e alerta",
                "custo": 500,
                "perda_restante": 600,
                "iot": True,
                "explicacao": (
                    "A bomba liga e desliga sozinha pelo nível da caixa e nunca "
                    "trabalha a seco. Se algo foge do normal, o síndico recebe um aviso."
                ),
            },
        ],
        "conceito": {
            "titulo": "Controle automático por sensor de nível",
            "resumo": (
                "Um sensor mede quanto de água há no reservatório e comanda a bomba "
                "automaticamente."
            ),
            "como_funciona": [
                "Um sensor de nível fica dentro da caixa d'água.",
                "Um controlador conectado liga a bomba quando o nível baixa.",
                "Quando a caixa enche, a bomba desliga sozinha.",
                "Nível estranho ou bomba ligada sem água geram alerta no celular.",
            ],
            "por_que_economiza": (
                "Acaba o desperdício de água e a bomba dura muito mais, sem depender "
                "de alguém vigiando."
            ),
        },
    },
    {
        "numero": 21,
        "trilha": "predial",
        "ordem": 5,
        "setor": "Instalação elétrica",
        "titulo": "O quadro de energia que esquenta",
        "problema": (
            "No edifício, disjuntores desarmam sem motivo aparente e alguns "
            "equipamentos já queimaram. Um eletricista notou cheiro de queimado "
            "perto de um quadro, mas não achou nada na hora."
        ),
        "perda_atual": 10000,
        "vozes": [
            {
                "nome": "André",
                "papel": "Engenheiro do prédio",
                "fala": "Para resolver de vez, só refazendo toda a parte elétrica.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Refazer tudo é caro e demorado. Se medirmos temperatura e "
                    "corrente nos quadros, descobrimos exatamente qual circuito está com problema."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Refazer toda a instalação elétrica do prédio",
                "custo": 9000,
                "perda_restante": 2000,
                "iot": False,
                "explicacao": (
                    "O problema foi resolvido, mas a obra custou muito e trocou "
                    "fiação que ainda estava boa. Uma decisão cara tomada sem saber "
                    "onde estava a falha."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar sensores de temperatura e corrente nos quadros elétricos",
                "custo": 700,
                "perda_restante": 1500,
                "iot": True,
                "explicacao": (
                    "Os sensores mostraram uma conexão frouxa esquentando no quadro "
                    "do 3º andar sempre que o ar-condicionado ligava. O reparo foi "
                    "simples e o problema acabou."
                ),
            },
            {
                "letra": "c",
                "texto": "Contratar uma inspeção com câmera térmica uma vez por ano",
                "custo": 300,
                "perda_restante": 7000,
                "iot": False,
                "explicacao": (
                    "A inspeção é útil, mas mostra só aquele dia. O aquecimento "
                    "acontecia em horários de pico e continuou causando desligamentos."
                ),
            },
        ],
        "conceito": {
            "titulo": "Monitoramento elétrico contínuo",
            "resumo": (
                "Sensores dentro dos quadros elétricos vigiam temperatura e corrente "
                "o tempo todo e avisam antes de um problema virar acidente."
            ),
            "como_funciona": [
                "Sensores pequenos são presos nos cabos e disjuntores mais importantes.",
                "Eles medem a temperatura e quanta corrente passa por cada circuito.",
                "As leituras vão para um painel que mostra cada quadro do prédio.",
                "Aquecimento ou sobrecarga geram alerta para a manutenção.",
            ],
            "por_que_economiza": (
                "Você conserta só o ponto com defeito, evita equipamentos queimados "
                "e reduz o risco de incêndio."
            ),
        },
    },

    # ======================= Trilha: Educação e Gestão Pública =======================
    {
        "numero": 22,
        "trilha": "publica",
        "ordem": 1,
        "setor": "Iluminação pública",
        "titulo": "Postes acesos durante o dia",
        "problema": (
            "A prefeitura paga caro pela iluminação pública. Muitos postes ficam "
            "acesos de dia, outros ficam apagados à noite por semanas, e a "
            "equipe só descobre quando a população reclama."
        ),
        "perda_atual": 25000,
        "vozes": [
            {
                "nome": "Secretário Paulo",
                "papel": "Secretaria de Obras",
                "fala": "Quando o cidadão ligar reclamando, a gente manda a equipe. Sempre foi assim.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Esperar reclamação é descobrir tarde. Se cada poste avisasse "
                    "quando está com problema, a equipe iria direto ao ponto certo."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Esperar as reclamações da população pelo telefone da prefeitura",
                "custo": 0,
                "perda_restante": 25000,
                "iot": False,
                "explicacao": (
                    "Nada mudou. Ninguém liga para reclamar de poste aceso de dia, "
                    "então o desperdício continuou, e ruas escuras demoram a ser consertadas."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar controladores conectados nos postes (telegestão)",
                "custo": 4000,
                "perda_restante": 5000,
                "iot": True,
                "explicacao": (
                    "Cada poste liga e desliga pelo horário do pôr do sol e diminui a "
                    "luz de madrugada. Lâmpada queimada aparece no mapa no mesmo dia."
                ),
            },
            {
                "letra": "c",
                "texto": "Fazer um mutirão anual para trocar os relés de todos os postes",
                "custo": 6000,
                "perda_restante": 15000,
                "iot": False,
                "explicacao": (
                    "Logo depois do mutirão a situação melhorou. Mas ao longo do ano "
                    "novos defeitos aparecem e ninguém fica sabendo até o próximo mutirão."
                ),
            },
        ],
        "conceito": {
            "titulo": "Telegestão de iluminação pública",
            "resumo": (
                "Cada poste ganha um pequeno controlador conectado, que pode ser "
                "comandado à distância e informa se está funcionando."
            ),
            "como_funciona": [
                "Um controlador é encaixado no topo de cada poste.",
                "Os controladores conversam por uma rede sem fio de longo alcance.",
                "A central define horários e a intensidade da luz em cada rua.",
                "Postes com defeito aparecem num mapa para a equipe de manutenção.",
            ],
            "por_que_economiza": (
                "A cidade gasta energia só quando precisa, e a manutenção vai direto "
                "aos postes com defeito, sem rondas às cegas."
            ),
        },
    },
    {
        "numero": 23,
        "trilha": "publica",
        "ordem": 3,
        "setor": "Coleta de lixo",
        "titulo": "O caminhão de lixo que passa à toa",
        "problema": (
            "Os caminhões de coleta seguem sempre a mesma rota. Em algumas ruas "
            "os contêineres estão quase vazios; em outras, transbordam antes de o "
            "caminhão passar, com lixo espalhado na calçada."
        ),
        "perda_atual": 18000,
        "vozes": [
            {
                "nome": "Graça",
                "papel": "Limpeza urbana",
                "fala": "Se tem lixo na rua, é só aumentar o número de passagens do caminhão.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Passar mais vezes em contêiner vazio é gastar diesel à toa. Se "
                    "soubéssemos quais estão cheios, a rota seria outra a cada dia."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Colocar sensores de nível nos contêineres e montar a rota pelos mais cheios",
                "custo": 2500,
                "perda_restante": 4000,
                "iot": True,
                "explicacao": (
                    "A rota do dia passou a incluir só os contêineres que precisam. "
                    "Os caminhões rodam menos e as calçadas ficaram limpas."
                ),
            },
            {
                "letra": "b",
                "texto": "Manter a rota fixa como está",
                "custo": 0,
                "perda_restante": 18000,
                "iot": False,
                "explicacao": (
                    "Tudo continua igual: viagens desnecessárias em alguns bairros e "
                    "lixo acumulado em outros."
                ),
            },
            {
                "letra": "c",
                "texto": "Aumentar o número de passagens do caminhão em todas as ruas",
                "custo": 8000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "O lixo espalhado diminuiu, mas o gasto com combustível e equipe "
                    "subiu muito, inclusive em ruas que não precisavam."
                ),
            },
        ],
        "conceito": {
            "titulo": "Coleta inteligente com sensores de nível",
            "resumo": (
                "Contêineres conectados informam o quanto estão cheios, e o sistema "
                "monta a melhor rota a cada dia."
            ),
            "como_funciona": [
                "Um sensor na tampa mede a distância até o lixo e calcula o nível.",
                "O contêiner envia esse nível algumas vezes por dia.",
                "O sistema escolhe os contêineres que precisam de coleta.",
                "O motorista recebe a rota otimizada no tablet do caminhão.",
            ],
            "por_que_economiza": (
                "Menos quilômetros rodados, menos combustível e ruas mais limpas, com "
                "a mesma frota."
            ),
        },
    },
    {
        "numero": 24,
        "trilha": "publica",
        "ordem": 2,
        "setor": "Escolas municipais",
        "titulo": "A conta de luz das escolas nas férias",
        "problema": (
            "A rede municipal tem 40 escolas. A conta de energia é alta até em "
            "férias e feriados, porque aparelhos de ar-condicionado e luzes ficam "
            "ligados sem ninguém nas salas."
        ),
        "perda_atual": 14000,
        "vozes": [
            {
                "nome": "Professora Ana",
                "papel": "Secretaria de Educação",
                "fala": "Vou mandar um técnico rodar as escolas toda sexta desligando tudo.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "São 40 escolas. Com medição e controle à distância, dá pra "
                    "desligar tudo de uma vez e ver qual escola mais gasta."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Mandar um técnico visitar as escolas toda sexta para desligar tudo",
                "custo": 4000,
                "perda_restante": 7000,
                "iot": False,
                "explicacao": (
                    "O técnico não consegue passar em todas as escolas, e durante a "
                    "semana o desperdício continua nas salas vazias."
                ),
            },
            {
                "letra": "b",
                "texto": "Trocar todos os aparelhos por modelos mais econômicos",
                "custo": 9000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "Os aparelhos novos gastam menos, mas continuam ligados à toa. "
                    "A parcela da troca ficou maior que a economia."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar medidores e controle remoto dos aparelhos por horário de aula",
                "custo": 2000,
                "perda_restante": 3000,
                "iot": True,
                "explicacao": (
                    "Os aparelhos só funcionam no horário de aula e desligam sozinhos "
                    "nas férias. O painel mostrou duas escolas com fiação desperdiçando "
                    "energia, que foram corrigidas."
                ),
            },
        ],
        "conceito": {
            "titulo": "Gestão de energia em várias unidades",
            "resumo": (
                "Medidores e controladores conectados permitem ver e comandar o "
                "consumo de muitos prédios a partir de um único painel."
            ),
            "como_funciona": [
                "Cada escola recebe um medidor de energia conectado.",
                "Os aparelhos ganham controladores que obedecem ao calendário escolar.",
                "Um painel compara o consumo de todas as escolas.",
                "Consumo fora do horário de aula gera alerta para a secretaria.",
            ],
            "por_que_economiza": (
                "O dinheiro público deixa de pagar energia de sala vazia, e a "
                "secretaria sabe onde agir primeiro."
            ),
        },
    },
    {
        "numero": 25,
        "trilha": "publica",
        "ordem": 4,
        "setor": "Transporte público",
        "titulo": "Ônibus lotados e ônibus vazios",
        "problema": (
            "Algumas linhas de ônibus da cidade andam lotadas no horário de pico, "
            "enquanto outras rodam quase vazias. Os horários foram definidos há "
            "anos e nunca foram revistos com dados."
        ),
        "perda_atual": 16000,
        "vozes": [
            {
                "nome": "Rogério",
                "papel": "Secretaria de Mobilidade",
                "fala": "A solução é colocar mais ônibus no horário de pico em todas as linhas.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Nem toda linha precisa de mais ônibus. Contando os passageiros, "
                    "dá pra tirar de onde sobra e colocar onde falta."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Fazer uma pesquisa em papel com os passageiros a cada dois anos",
                "custo": 500,
                "perda_restante": 13000,
                "iot": False,
                "explicacao": (
                    "A pesquisa ajuda a entender opiniões, mas não mostra o "
                    "movimento real de cada horário. Pouca coisa mudou."
                ),
            },
            {
                "letra": "b",
                "texto": "Colocar contadores de passageiros e GPS nos ônibus para ajustar os horários",
                "custo": 2500,
                "perda_restante": 4500,
                "iot": True,
                "explicacao": (
                    "Os dados mostraram linhas vazias à tarde e superlotadas às 7h. "
                    "Os horários foram redistribuídos com a mesma frota, e a lotação caiu."
                ),
            },
            {
                "letra": "c",
                "texto": "Colocar mais ônibus no horário de pico em todas as linhas",
                "custo": 9000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "As linhas lotadas melhoraram, mas as que já andavam vazias "
                    "ganharam ainda mais ônibus vazios. O custo foi muito alto."
                ),
            },
        ],
        "conceito": {
            "titulo": "Contagem de passageiros e frota conectada",
            "resumo": (
                "Sensores nas portas contam quem sobe e desce, e o GPS mostra onde "
                "cada ônibus está, formando um retrato real do uso das linhas."
            ),
            "como_funciona": [
                "Sensores nas portas contam embarques e desembarques.",
                "O GPS associa cada contagem a um ponto e a um horário.",
                "O painel mostra a lotação de cada linha ao longo do dia.",
                "Os horários são ajustados para acompanhar a demanda real.",
            ],
            "por_que_economiza": (
                "Você atende melhor a população usando a frota que já existe, em vez "
                "de comprar mais ônibus."
            ),
        },
    },
    {
        "numero": 26,
        "trilha": "publica",
        "ordem": 5,
        "setor": "Defesa Civil",
        "titulo": "O bairro que alaga sem aviso",
        "problema": (
            "Em dias de chuva forte, alguns bairros alagam rapidamente. Moradores "
            "perdem móveis e carros, e a Defesa Civil só fica sabendo quando a "
            "água já subiu e os pedidos de socorro começam."
        ),
        "perda_atual": 30000,
        "vozes": [
            {
                "nome": "Coronel Silva",
                "papel": "Defesa Civil",
                "fala": "Nossa equipe é rápida. Quando chamarem, a gente chega.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Se o nível do rio e a chuva forem medidos o tempo todo, dá pra "
                    "avisar os moradores antes de a água chegar nas casas."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Limpar todos os bueiros e canais da cidade toda semana",
                "custo": 15000,
                "perda_restante": 14000,
                "iot": False,
                "explicacao": (
                    "A drenagem melhorou, mas o custo foi enorme. Em chuvas muito "
                    "fortes os bairros alagaram mesmo assim, e sem aviso."
                ),
            },
            {
                "letra": "b",
                "texto": "Agir quando chegarem as ligações de emergência",
                "custo": 0,
                "perda_restante": 30000,
                "iot": False,
                "explicacao": (
                    "Nada mudou: quando o socorro chega, os prejuízos já aconteceram."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar sensores de nível nos rios e medidores de chuva, com alerta por SMS",
                "custo": 3500,
                "perda_restante": 9000,
                "iot": True,
                "explicacao": (
                    "Com o rio subindo rápido, os moradores receberam um SMS uma hora "
                    "antes. Deu tempo de tirar carros e levantar móveis, e a equipe "
                    "já estava posicionada."
                ),
            },
        ],
        "conceito": {
            "titulo": "Sistema de alerta antecipado",
            "resumo": (
                "Sensores espalhados pela cidade medem chuva e nível da água e "
                "disparam alertas antes de o problema chegar."
            ),
            "como_funciona": [
                "Medidores de chuva e sensores de nível ficam em rios e canais.",
                "As leituras chegam à central a cada poucos minutos.",
                "O sistema compara com níveis de atenção e de perigo.",
                "Ao atingir o nível de atenção, moradores da área recebem um SMS.",
            ],
            "por_que_economiza": (
                "A população tem tempo de se proteger e a resposta da cidade fica "
                "mais rápida, reduzindo prejuízos e riscos à vida."
            ),
        },
    },

    # ======================= Trilha: Agronegócio =======================
    {
        "numero": 27,
        "trilha": "agro",
        "ordem": 3,
        "setor": "Pecuária leiteira",
        "titulo": "As vacas doentes descobertas tarde",
        "problema": (
            "Na fazenda de leite, quando uma vaca adoece, a produção dela cai "
            "vários dias antes de alguém perceber. Quando o tratamento começa, "
            "o leite perdido e os remédios já custaram caro."
        ),
        "perda_atual": 12000,
        "vozes": [
            {
                "nome": "Zé Carlos",
                "papel": "Capataz",
                "fala": "Melhor dar remédio preventivo pra todo o rebanho de uma vez.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Vaca doente se mexe e rumina menos, bem antes de aparecer a "
                    "doença. Com um colar de sensores, a gente vê isso cedo."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Dar antibiótico preventivo para o rebanho inteiro",
                "custo": 3000,
                "perda_restante": 5000,
                "iot": False,
                "explicacao": (
                    "Algumas doenças diminuíram, mas o leite com antibiótico não pode "
                    "ser vendido por dias. E remédio sem necessidade cria resistência."
                ),
            },
            {
                "letra": "b",
                "texto": "Colocar colares com sensores de atividade e ruminação nas vacas",
                "custo": 2000,
                "perda_restante": 2500,
                "iot": True,
                "explicacao": (
                    "O sistema avisou que três vacas estavam ruminando menos. O "
                    "veterinário tratou só elas, cedo, e a produção quase não caiu."
                ),
            },
            {
                "letra": "c",
                "texto": "Trazer o veterinário para examinar o rebanho toda semana",
                "custo": 5000,
                "perda_restante": 6000,
                "iot": False,
                "explicacao": (
                    "O veterinário ajuda, mas uma visita por semana não pega a "
                    "doença que começa no dia seguinte. O custo também ficou alto."
                ),
            },
        ],
        "conceito": {
            "titulo": "Monitoramento de saúde animal",
            "resumo": (
                "Sensores usados pelos animais registram comportamento e mostram "
                "sinais de doença antes que eles fiquem visíveis."
            ),
            "como_funciona": [
                "Cada vaca usa um colar com sensor de movimento.",
                "O colar registra quanto tempo ela caminha, descansa e rumina.",
                "Antenas no curral recebem os dados quando ela passa por perto.",
                "Mudança de comportamento gera alerta com o número do animal.",
            ],
            "por_que_economiza": (
                "O tratamento começa cedo e só nos animais que precisam: menos "
                "leite perdido e menos remédio."
            ),
        },
    },
    {
        "numero": 28,
        "trilha": "agro",
        "ordem": 2,
        "setor": "Armazenagem de grãos",
        "titulo": "O silo que estraga a safra",
        "problema": (
            "Os grãos guardados no silo da cooperativa estão esquentando e "
            "criando fungos em alguns pontos. Quando o problema aparece na "
            "descarga, parte da safra já perdeu valor."
        ),
        "perda_atual": 22000,
        "vozes": [
            {
                "nome": "Dona Neide",
                "papel": "Presidente da cooperativa",
                "fala": "Pra não arriscar, vamos vender tudo logo depois da colheita.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "Vender na colheita é vender no preço mais baixo. Se a gente "
                    "souber a temperatura dentro do silo, dá pra guardar com segurança."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Vender toda a safra logo após a colheita",
                "custo": 0,
                "perda_restante": 14000,
                "iot": False,
                "explicacao": (
                    "Os grãos não estragaram, mas foram vendidos no período em que o "
                    "preço é o mais baixo do ano. O prejuízo só mudou de forma."
                ),
            },
            {
                "letra": "b",
                "texto": "Instalar cabos de temperatura dentro do silo com ventilação automática",
                "custo": 2500,
                "perda_restante": 3000,
                "iot": True,
                "explicacao": (
                    "Os sensores mostraram um ponto quente no meio do silo. A "
                    "ventilação ligou sozinha e resfriou os grãos. A cooperativa "
                    "esperou o preço subir para vender."
                ),
            },
            {
                "letra": "c",
                "texto": "Remexer os grãos manualmente toda semana",
                "custo": 4000,
                "perda_restante": 12000,
                "iot": False,
                "explicacao": (
                    "Ajuda nas camadas de cima, mas o calor começa no fundo, onde "
                    "ninguém alcança. E o trabalho é pesado e arriscado."
                ),
            },
        ],
        "conceito": {
            "titulo": "Termometria de grãos com aeração automática",
            "resumo": (
                "Cabos com vários sensores atravessam o silo de cima a baixo e "
                "mostram a temperatura em cada camada dos grãos."
            ),
            "como_funciona": [
                "Cabos com sensores ficam pendurados dentro do silo.",
                "Cada sensor mede a temperatura e a umidade daquela camada.",
                "O sistema identifica pontos quentes, sinal de fungo ou umidade.",
                "Os ventiladores ligam sozinhos quando o ar de fora está adequado.",
            ],
            "por_que_economiza": (
                "A safra fica guardada com segurança e pode ser vendida na melhor "
                "época, sem perdas no armazém."
            ),
        },
    },
    {
        "numero": 29,
        "trilha": "agro",
        "ordem": 4,
        "setor": "Estufa",
        "titulo": "A estufa que cozinha as plantas",
        "problema": (
            "Na estufa de hortaliças, em dias quentes a temperatura sobe demais e "
            "as plantas murcham. Em dias frios e úmidos, aparecem doenças. As "
            "cortinas são abertas e fechadas em horários fixos."
        ),
        "perda_atual": 9000,
        "vozes": [
            {
                "nome": "Tiago",
                "papel": "Produtor",
                "fala": "Vou colocar ar-condicionado industrial e deixar ligado direto.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "O clima muda ao longo do dia. Se a estufa medir temperatura e "
                    "umidade, as cortinas podem abrir na hora certa, sozinhas."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Instalar climatização forte e deixar ligada o tempo todo",
                "custo": 6000,
                "perda_restante": 1500,
                "iot": False,
                "explicacao": (
                    "As plantas ficaram bem, mas a conta de energia disparou. Em "
                    "muitos momentos o aparelho gastava sem precisar."
                ),
            },
            {
                "letra": "b",
                "texto": "Colocar um funcionário para abrir e fechar as cortinas por horário",
                "custo": 2000,
                "perda_restante": 5000,
                "iot": False,
                "explicacao": (
                    "Horário fixo não acompanha o tempo de verdade. Num dia nublado "
                    "abre cedo demais; num dia quente, tarde demais."
                ),
            },
            {
                "letra": "c",
                "texto": "Instalar sensores de clima com cortinas e nebulização automáticas",
                "custo": 1500,
                "perda_restante": 1200,
                "iot": True,
                "explicacao": (
                    "As cortinas abrem quando passa de 28 °C e a nebulização liga "
                    "quando o ar fica seco. As perdas caíram com pouco gasto de energia."
                ),
            },
        ],
        "conceito": {
            "titulo": "Controle climático automatizado",
            "resumo": (
                "Sensores medem o clima dentro da estufa e comandam cortinas, "
                "ventiladores e nebulizadores para manter o ambiente ideal."
            ),
            "como_funciona": [
                "Sensores medem temperatura, umidade e luz dentro da estufa.",
                "O controlador compara com a faixa ideal de cada cultura.",
                "Motores abrem ou fecham as cortinas e ligam a nebulização.",
                "O produtor acompanha e ajusta tudo pelo celular.",
            ],
            "por_que_economiza": (
                "A planta fica sempre no clima certo, gastando energia e água só "
                "quando é necessário."
            ),
        },
    },
    {
        "numero": 30,
        "trilha": "agro",
        "ordem": 5,
        "setor": "Lavoura",
        "titulo": "A praga descoberta tarde demais",
        "problema": (
            "Na lavoura de soja, pragas aparecem em manchas e se espalham "
            "rápido. Quando o monitor de campo encontra, já há estrago. Para "
            "garantir, a fazenda tem aplicado defensivo em tudo."
        ),
        "perda_atual": 18000,
        "vozes": [
            {
                "nome": "Agrônomo Lucas",
                "papel": "Consultor técnico",
                "fala": "Aplicação em toda a área a cada quinze dias resolve.",
            },
            {
                "nome": "Alex",
                "papel": "Analista de dados",
                "fala": (
                    "A praga não está em toda a área. Se as armadilhas contarem os "
                    "insetos sozinhas, dá pra aplicar só onde precisa."
                ),
            },
        ],
        "opcoes": [
            {
                "letra": "a",
                "texto": "Pedir para o monitor de campo percorrer a lavoura uma vez por semana",
                "custo": 2500,
                "perda_restante": 9000,
                "iot": False,
                "explicacao": (
                    "A fazenda é grande e o monitor não vê tudo. Entre uma visita e "
                    "outra, a praga avança."
                ),
            },
            {
                "letra": "b",
                "texto": "Aplicar defensivo na lavoura inteira a cada 15 dias",
                "custo": 9000,
                "perda_restante": 5000,
                "iot": False,
                "explicacao": (
                    "A praga foi controlada, mas o gasto com produto foi enorme e boa "
                    "parte foi aplicada onde não havia praga nenhuma."
                ),
            },
            {
                "letra": "c",
                "texto": "Espalhar armadilhas conectadas que contam os insetos e mostram onde aplicar",
                "custo": 2000,
                "perda_restante": 3000,
                "iot": True,
                "explicacao": (
                    "As armadilhas mostraram a praga crescendo num canto da lavoura. "
                    "A aplicação foi feita só ali, cedo, e o resto da área ficou protegido."
                ),
            },
        ],
        "conceito": {
            "titulo": "Monitoramento de pragas com armadilhas inteligentes",
            "resumo": (
                "Armadilhas com câmera e conexão contam os insetos capturados e "
                "mostram, num mapa, onde a praga está crescendo."
            ),
            "como_funciona": [
                "Armadilhas com câmera são espalhadas pela lavoura.",
                "Todo dia, elas fotografam e contam os insetos presos.",
                "As contagens vão pela rede de longo alcance até a nuvem.",
                "O mapa mostra os pontos que passaram do nível de controle.",
            ],
            "por_que_economiza": (
                "O defensivo é usado só onde e quando precisa: menos produto, menos "
                "custo e a lavoura protegida."
            ),
        },
    },
]
