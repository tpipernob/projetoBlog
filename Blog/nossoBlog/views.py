from django.shortcuts import render
from .models import *

def postagem(request, template_name='index.html'):
    postagem = Postagem.objects.all()
    postagens = {'lista': postagem}
    return render(request, template_name, postagens)