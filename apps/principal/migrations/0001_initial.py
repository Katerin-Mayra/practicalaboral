# Generated by Django 2.2 on 2021-01-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
    ]