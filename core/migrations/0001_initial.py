# Generated by Django 5.0.2 on 2024-04-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ferramentas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20, null=True)),
                ('grupo', models.CharField(max_length=20, null=True)),
                ('montadora', models.CharField(max_length=50, null=True)),
                ('aplicacao', models.CharField(max_length=50, null=True)),
                ('quantidade', models.CharField(max_length=20)),
                ('observacoes', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'ferramentas',
            },
        ),
        migrations.CreateModel(
            name='Pecas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20, null=True)),
                ('grupo', models.CharField(max_length=20, null=True)),
                ('montadora', models.CharField(max_length=50, null=True)),
                ('aplicacao', models.CharField(max_length=50, null=True)),
                ('quantidade', models.CharField(max_length=20)),
                ('observacoes', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'pecas',
            },
        ),
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
            options={
                'db_table': 'faltantes',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255, null=True)),
            ],
        ),
    ]
