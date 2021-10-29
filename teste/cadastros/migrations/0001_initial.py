# Generated by Django 2.2.12 on 2021-10-28 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.IntegerField()),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Produto')),
            ],
        ),
    ]
