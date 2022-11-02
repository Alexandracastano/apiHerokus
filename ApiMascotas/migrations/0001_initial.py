# Generated by Django 4.1.2 on 2022-10-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=11)),
                ('direccion', models.CharField(max_length=80)),
                ('nombre', models.CharField(max_length=60)),
                ('Edad', models.PositiveIntegerField(default=0)),
                ('Raza', models.CharField(max_length=60)),
                ('tamaño', models.CharField(max_length=50)),
                ('Genero', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=60)),
                ('situacion', models.CharField(max_length=200)),
            ],
        ),
    ]
