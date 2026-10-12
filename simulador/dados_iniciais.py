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
"""

CENARIOS = [
    {
        "numero": 1,
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
