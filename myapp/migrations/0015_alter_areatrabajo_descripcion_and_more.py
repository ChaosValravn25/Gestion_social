# Generated by Django 4.2.16 on 2024-10-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_documento_descripcion_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areatrabajo',
            name='descripcion',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='documento',
            name='descripcion_documento',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
