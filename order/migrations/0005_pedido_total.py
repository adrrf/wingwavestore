# Generated by Django 4.2.5 on 2023-11-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_pedido_apellido_pedido_email_pedido_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
