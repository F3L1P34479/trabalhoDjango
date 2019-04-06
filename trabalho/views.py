from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.
# Cria uma classe com herança de TemplateView para exibir um arquivo HTML normal
# (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "index.html"

class SobreView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "sobre.html"

class ContatoView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "contato.html"

class CadastrosView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "cadastros.html"

class CurriculoView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "curriculo.html"
