# Generated by Django 2.2 on 2020-06-22 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_custom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ejemplar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_custom.Ejemplar'),
        ),
    ]
