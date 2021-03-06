# Generated by Django 2.2 on 2019-04-18 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('average_cost', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('date_released', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('product_image', models.ImageField(default='default.jpg', upload_to='product_images')),
            ],
        ),
    ]
