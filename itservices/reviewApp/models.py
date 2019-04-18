from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
	name=models.CharField(max_length=100)
	brand=models.CharField(max_length=100)
	average_cost=models.DecimalField(decimal_places=2,max_digits=6)
	category=models.CharField(max_length=100)
	date_released=models.DateTimeField(default=timezone.now)
	description=models.TextField()
	product_image=models.ImageField(default='default.jpg', upload_to='product_images')

	def __str__(self):
		return self.name #The text which is shown on the list.