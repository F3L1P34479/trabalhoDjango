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
]
