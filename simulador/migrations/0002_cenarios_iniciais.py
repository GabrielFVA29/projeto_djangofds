"""
Grava os cenários iniciais no banco de dados.
Roda sozinha no `python manage.py migrate` (inclusive no deploy, pelo build.sh).
"""
from django.db import migrations

from simulador.dados_iniciais import CENARIOS


def criar_cenarios(apps, schema_editor):
    Cenario = apps.get_model("simulador", "Cenario")
    Voz = apps.get_model("simulador", "Voz")
    Opcao = apps.get_model("simulador", "Opcao")

    for dados in CENARIOS:
        conceito = dados["conceito"]
        cenario, _ = Cenario.objects.update_or_create(
            numero=dados["numero"],
            defaults={
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


def apagar_cenarios(apps, schema_editor):
    apps.get_model("simulador", "Cenario").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("simulador", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(criar_cenarios, apagar_cenarios),
    ]
