from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Review(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE, default='1')
	rating=IntegerField(
		default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
	review_text=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f' Review by {self.author.username} of the {self.product}'
