# Generated by Django 3.2.20 on 2023-07-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, verbose_name='Nombre')),
                ('edad', models.IntegerField(blank=True, verbose_name='Edad')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=10, verbose_name='sexo')),
                ('nacionalidad', models.CharField(blank=True, max_length=150, verbose_name='Nacionalidad')),
            ],
        ),
    ]
