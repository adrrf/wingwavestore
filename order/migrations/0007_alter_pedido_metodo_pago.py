# Generated by Django 4.2.5 on 2023-11-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_pedido_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='metodo_pago',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
