# Generated by Django 2.2 on 2020-06-25 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(default=None, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=25)),
                ('numero', models.IntegerField()),
                ('ciudad', models.CharField(max_length=25)),
                ('comuna', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('descuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('web', models.CharField(blank=True, default='None', max_length=150, null=True)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Direccion')),
                ('telefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Categoria')),
                ('productosssss', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.Venta')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Direccion')),
                ('telefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Telefono')),
            ],
        ),
    ]
