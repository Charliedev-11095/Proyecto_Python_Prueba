# Generated by Django 4.0.5 on 2022-07-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0008_alter_alumnos_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('titulo', models.CharField(max_length=100, null=True, verbose_name='Titulo')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Archivos')),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'ordering': ['-created'],
            },
        ),
    ]
