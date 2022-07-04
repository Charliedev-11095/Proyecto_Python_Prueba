# Generated by Django 4.0.5 on 2022-07-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_comentariocontacto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-created'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='comentariocontacto',
            options={'ordering': ['-created'], 'verbose_name': 'Comentario Contacto', 'verbose_name_plural': 'Comentarios Contactos'},
        ),
        migrations.AlterField(
            model_name='comentariocontacto',
            name='usuario',
            field=models.TextField(verbose_name='Alumno'),
        ),
    ]
