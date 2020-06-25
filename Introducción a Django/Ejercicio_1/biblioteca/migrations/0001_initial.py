# Generated by Django 2.2 on 2020-06-06 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplares',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('localizacion', models.CharField(max_length=30)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Autores')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('editorial', models.CharField(max_length=20)),
                ('paginas', models.IntegerField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Autores')),
                ('id_ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Ejemplares')),
            ],
        ),
        migrations.AddField(
            model_name='ejemplares',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Usuarios'),
        ),
    ]
