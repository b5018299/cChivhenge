# Generated by Django 2.2 on 2019-04-19 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0004_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]
