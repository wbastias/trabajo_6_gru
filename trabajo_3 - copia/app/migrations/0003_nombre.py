# Generated by Django 3.1.5 on 2021-01-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_temperatura_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('temperatura', models.IntegerField()),
                ('fecha_de_emicion', models.DateField()),
            ],
        ),
    ]
