# Generated by Django 2.2 on 2019-04-19 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0008_remove_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='reviewApp.Product'),
        ),
    ]
