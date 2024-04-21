# Generated by Django 5.0.2 on 2024-03-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PecasFaltantes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20, null=True)),
                ('pedido', models.CharField(max_length=20)),
                ('quantidade', models.CharField(max_length=20)),
                ('observacoes', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]