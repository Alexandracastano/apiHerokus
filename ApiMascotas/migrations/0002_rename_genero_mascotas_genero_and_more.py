# Generated by Django 4.1.2 on 2022-11-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiMascotas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascotas',
            old_name='Genero',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='mascotas',
            old_name='Raza',
            new_name='raza',
        ),
        migrations.RemoveField(
            model_name='mascotas',
            name='Edad',
        ),
        migrations.AddField(
            model_name='mascotas',
            name='edad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
