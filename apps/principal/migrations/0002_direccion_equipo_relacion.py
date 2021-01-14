# Generated by Django 2.2 on 2021-01-13 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DireccionIP', models.GenericIPAddressField(db_index=True, null=True, verbose_name='IP Address')),
                ('PuertaEnlace', models.GenericIPAddressField()),
                ('Mascara', models.GenericIPAddressField()),
                ('Permisos', models.CharField(max_length=50)),
                ('Grupo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreHost', models.CharField(max_length=50)),
                ('SistemaOperativo', models.CharField(max_length=50)),
                ('MAC', models.CharField(max_length=50)),
                ('MAC1', models.CharField(max_length=50)),
                ('Adaptador', models.CharField(max_length=50)),
                ('direccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Direccion')),
            ],
        ),
    ]