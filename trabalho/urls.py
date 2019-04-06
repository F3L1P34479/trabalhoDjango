# Módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
    # path(
    #   'caminho/da/url',
    #   ClasseLáDoView.as_view(),
    #    name='nomeDessaUrl')
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('cadastros/', CadastrosView.as_view(), name="cadastros"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo"),
]
