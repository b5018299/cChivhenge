# Generated by Django 2.2 on 2019-04-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='average_cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
