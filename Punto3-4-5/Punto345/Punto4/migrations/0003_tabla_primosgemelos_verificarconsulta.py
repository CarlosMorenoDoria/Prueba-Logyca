# Generated by Django 3.1 on 2020-09-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Punto4', '0002_auto_20200902_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabla_primosgemelos',
            name='verificarconsulta',
            field=models.IntegerField(default=0),
        ),
    ]