from django.shortcuts import render
from django.shortcuts import render
# Importa todas as classes do models.py
from .models import *

# importa a função que vai chamar as urlspelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir uitlizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

#Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

#Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir um arquivo HTML normal
# (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "cadastros/index.html"
