# Generated by Django 4.2.7 on 2023-12-05 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_mensajereclamacion_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamacion',
            name='mensajes',
        ),
    ]