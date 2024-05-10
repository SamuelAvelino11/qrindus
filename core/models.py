from django.db import models

import photos


# Create your models here.
class ferramentas(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=50, null=False)
    cor = models.CharField(max_length=20, null=True)
    grupo = models.CharField(max_length=20, null=True)
    montadora = models.CharField(max_length=50, null=True)
    aplicacao = models.CharField(max_length=50, null=True)
    quantidade = models.CharField(max_length=20, null=False)
    observacoes = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'ferramentas'


class PecasFaltantes(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=50, null=False)
    cor = models.CharField(max_length=20, null=True)
    pedido = models.CharField(max_length=20, null=False)
    quantidade = models.CharField(max_length=20, null=False)
    observacoes = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'faltantes'

class Pecas(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=50, null=False)
    cor = models.CharField(max_length=20, null=True)
    grupo = models.CharField(max_length=20, null=True)
    montadora = models.CharField(max_length=50, null=True)
    aplicacao = models.CharField(max_length=50, null=True)
    quantidade = models.CharField(max_length=20, null=False)
    observacoes = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'pecas'



class Photo(models.Model):
    image = models.ImageField(upload_to='photo/'),
    description = models.TextField(max_length=255, null=True)

class faltantes(models.Model):
    id = models.AutoField(primary_key=True)
    peca = models.TextField(max_length=100, null=False)
    cor = models.TextField(max_length=20, null=True)
    qtd = models.IntegerField(1000)

class pedidosfaltantes(models.Model):
    id = models.AutoField(primary_key=True)
    numerodopedido = models.TextField(null=False)
    dataLancamento = models.DateField(verbose_name=None)
    pecas = models.ManyToManyField(faltantes)

    class Meta:
        db_table = 'pedidosfaltantes'

