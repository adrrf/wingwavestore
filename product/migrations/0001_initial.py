from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=255)),
                ('precio', models.FloatField()),
                ('descripcion', models.CharField(max_length=255)),
                ('departamento', models.CharField(max_length=255)),
                ('seccion', models.CharField(max_length=255)),
                ('fabricante', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
