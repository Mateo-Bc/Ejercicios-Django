# Generated by Django 2.2 on 2020-06-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_custom', '0009_auto_20200622_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
