# Generated by Django 2.2.12 on 2021-11-03 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_auto_20211101_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Cliente'),
        ),
    ]
