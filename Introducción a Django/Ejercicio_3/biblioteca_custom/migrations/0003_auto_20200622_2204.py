# Generated by Django 2.2 on 2020-06-22 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_custom', '0002_auto_20200622_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ejemplar',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='biblioteca_custom.Ejemplar'),
        ),
    ]
