# Generated by Django 4.2.16 on 2024-10-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_areatrabajo_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areatrabajo',
            name='descripcion',
            field=models.TextField(default=''),
        ),
    ]
