# Generated by Django 2.0.5 on 2018-06-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CDC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomoneta',
            name='Tipo',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
