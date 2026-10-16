"""
Grava as 6 trilhas e as 30 rodadas (5 por trilha) no banco de dados.
Roda sozinha no `python manage.py migrate` (inclusive no deploy, pelo build.sh).

Os cenários 1 a 5, que já existiam, continuam com o mesmo número; só passam
a pertencer a uma trilha. Assim as partidas antigas do ranking não se perdem.
"""
from django.db import migrations

from simulador.dados_iniciais import CENARIOS, TRILHAS


def criar_trilhas_e_cenarios(apps, schema_editor):
    Trilha = apps.get_model("simulador", "Trilha")
    Cenario = apps.get_model("simulador", "Cenario")
    Voz = apps.get_model("simulador", "Voz")
    Opcao = apps.get_model("simulador", "Opcao")

    trilhas = {}
    for dados in TRILHAS:
        trilha, _ = Trilha.objects.update_or_create(
            slug=dados["slug"],
            defaults={
                "numero": dados["numero"],
                "nome": dados["nome"],
                "icone": dados["icone"],
                "descricao": dados["descricao"],
                "exemplos": dados["exemplos"],
                "diagnostico": dados["diagnostico"],
            },
        )
        trilhas[trilha.slug] = trilha

    for dados in CENARIOS:
        conceito = dados["conceito"]
        cenario, _ = Cenario.objects.update_or_create(
            numero=dados["numero"],
            defaults={
                "trilha": trilhas[dados["trilha"]],
                "ordem": dados["ordem"],
                "setor": dados["setor"],
                "titulo": dados["titulo"],
                "problema": dados["problema"],
                "perda_atual": dados["perda_atual"],
                "conceito_titulo": conceito["titulo"],
                "conceito_resumo": conceito["resumo"],
                "conceito_passos": "\n".join(conceito["como_funciona"]),
                "conceito_economia": conceito["por_que_economiza"],
            },
        )
        cenario.vozes.all().delete()
        for ordem, voz in enumerate(dados["vozes"]):
            Voz.objects.create(cenario=cenario, ordem=ordem, **voz)
        for opcao in dados["opcoes"]:
            Opcao.objects.update_or_create(
                cenario=cenario,
                letra=opcao["letra"],
                defaults={
                    "texto": opcao["texto"],
                    "custo": opcao["custo"],
                    "perda_restante": opcao["perda_restante"],
                    "usa_iot": opcao["iot"],
                    "explicacao": opcao["explicacao"],
                },
            )


class Migration(migrations.Migration):

    dependencies = [
        ("simulador", "0003_trilhas"),
    ]

    operations = [
        migrations.RunPython(criar_trilhas_e_cenarios, migrations.RunPython.noop),
    ]
