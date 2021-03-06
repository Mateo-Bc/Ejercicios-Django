# Generated by Django 2.2 on 2020-06-18 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_custom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplares',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='libros',
            name='id_ejemplar',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='id_ejemplar',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='biblioteca_custom.Ejemplares'),
        ),
        migrations.AlterField(
            model_name='ejemplares',
            name='id_libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_custom.Libros'),
        ),
    ]
