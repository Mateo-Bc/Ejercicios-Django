# Generated by Django 2.2 on 2020-07-02 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20200702_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='producto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto'),
        ),
    ]
