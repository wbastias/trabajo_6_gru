# Generated by Django 3.1.5 on 2021-01-14 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nombre',
            old_name='temperatura',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='nombre',
            old_name='nombre',
            new_name='personas',
        ),
    ]
