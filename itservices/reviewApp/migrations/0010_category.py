# Generated by Django 2.2 on 2019-04-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0009_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]