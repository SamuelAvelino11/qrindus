import requests
from django.shortcuts import render, redirect
from .models import Photo, PedidoDeSeparacao
from .models import ferramentas
from .models import faltantes

# Create your views here.
def view_login(request):
    return render(request, 'login.html')

def menu(request):
    return render(request, 'Menu.html')

def views_crudFerr(request):
    ferro = ferramentas.objects.all()
    dados= ferramentas.objects.all()
    return render(request,'crud.html', {'dados':dados})

def submit_Ferr(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        cor = request.POST.get('cor')
        grupo = request.POST.get('grupo')
        montadora = request.POST.get('montadora')
        aplicacao = request.POST.get('aplicacao')
        quantidade = request.POST.get('quantidade')
        observacoes = request.POST.get('observacoes')

        ferros = ferramentas(
            item=item,
            cor=cor,
            grupo=grupo,
            montadora=montadora,
            aplicacao=aplicacao,
            quantidade=quantidade,
            observacoes=observacoes
        )
        ferros.save()
        dados = ferramentas.objects.all()
    return render(request, 'crud.html', {'dados':dados})

def Pedido(request):
    return render(request, 'cad_pedidos.html')

def submitPedido(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        observacoes = request.POST.get('observacao')
        dataRecebimento = request.POST.get('dataRecebimento')
        dataEntrega = request.POST.get('dataEntrega')

        numPed = PedidoDeSeparacao(
            numero = numero,
            observacoes = observacoes,
            dataRecebimento = dataRecebimento,
            dataEntrega = dataEntrega
        )
        numPed.save()
        dados = PedidoDeSeparacao.objects.all()
    return render(request,'Pedidos.html', {'dados':dados})
