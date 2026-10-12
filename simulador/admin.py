from django.contrib import admin

from .models import Cenario, Decisao, Opcao, Rodada, Voz


class VozInline(admin.TabularInline):
    model = Voz
    extra = 0


class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 0


@admin.register(Cenario)
class CenarioAdmin(admin.ModelAdmin):
    list_display = ("numero", "titulo", "setor", "perda_atual")
    inlines = [VozInline, OpcaoInline]


class DecisaoInline(admin.TabularInline):
    model = Decisao
    extra = 0


@admin.register(Rodada)
class RodadaAdmin(admin.ModelAdmin):
    list_display = ("jogador", "empresa", "iniciada_em", "finalizada_em")
    inlines = [DecisaoInline]
