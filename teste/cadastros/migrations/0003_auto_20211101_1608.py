# Generated by Django 2.2.12 on 2021-11-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20211028_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
