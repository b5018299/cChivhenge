# Generated by Django 2.2 on 2019-04-19 16:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='reviewApp.Product'),
            preserve_default=False,
        ),
    ]
