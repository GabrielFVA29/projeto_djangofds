from django.urls import path
from . import views

app_name = "simulador"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("como-funciona/", views.como_funciona, name="como_funciona"),
    path("comecar/", views.comecar, name="comecar"),
    path("cenario/<int:numero>/", views.cenario, name="cenario"),
    path("cenario/<int:numero>/resultado/", views.resultado, name="resultado"),
    path("relatorio/", views.relatorio, name="relatorio"),
    path("ranking/", views.ranking, name="ranking"),
    path("rodada/<int:rodada_id>/", views.rodada_detalhe, name="rodada"),
]
