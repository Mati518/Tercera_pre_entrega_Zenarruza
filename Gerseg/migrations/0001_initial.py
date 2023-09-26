# Generated by Django 4.2.5 on 2023-09-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bancas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medidas', models.IntegerField()),
                ('regulable', models.BooleanField()),
                ('materialRecubrimiento', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Barras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medidas', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('tipo', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=60)),
                ('modelo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=60)),
                ('nUsuario', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Discos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medidas', models.IntegerField()),
                ('tipo', models.CharField(max_length=60)),
                ('peso', models.IntegerField()),
                ('marca', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Racks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medidas', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('marca', models.CharField(max_length=60)),
            ],
        ),
    ]
