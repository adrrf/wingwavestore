# Generated by Django 4.2.5 on 2023-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_pedido_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='stripe_id',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
