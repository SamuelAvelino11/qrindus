from django.shortcuts import render, redirect
from .models import Photo
from .models import ferramentas

# Create your views here.
def view_login(request):
    return render(request, 'login.html')

def menu(request):
    photos = Photo.objects.all()
    return render(request, 'Menu.html', {'photos': photos})

def views_crudFerr(request):
    return render(request,'crud.html')

def submit_Ferr(request):
    if request.method == 'POST':
        item = request.POST['item']
        cor = request.POST['cor']
        grupo = request.POST['grupo']
        montadora = request.POST['montadora']
        aplicacao = request.POST['aplicacao']
        quantidade = request.POST['quantidade']
        observacoes = request.POST['observacoes']

        #ferramentas.item=item
        #ferramentas.cor=cor
        #ferramentas.grupo=grupo
        #ferramentas.montadora=montadora
        #ferramentas.quantidade=quantidade
        #ferramentas.aplicacao=aplicacao
        #ferramentas.observacoes=observacoes
        #ferramentas.save()
        fer = ferramentas(
            item=item,
            cor=cor,
            grupo=grupo,
            montadora=montadora,
            aplicacao=aplicacao,
            quantidade=quantidade,
            observacoes=observacoes
        )
        fer.save()
    return redirect('/')

