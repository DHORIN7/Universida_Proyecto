# Generated by Django 4.2.5 on 2023-10-23 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0002_rename_asignacion_id_lineaasignacion_asignacion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignacion',
            options={'ordering': ['id'], 'verbose_name': 'Asignacion', 'verbose_name_plural': 'Asignaciones'},
        ),
    ]
