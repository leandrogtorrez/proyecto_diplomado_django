# Generated by Django 5.1.4 on 2024-12-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='fecha_asignacion',
            field=models.DateTimeField(),
        ),
    ]
