from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	full_name=models.CharField(max_length=100)
	date_of_birth=models.DateTimeField(default=timezone.now)
	address=models.CharField(max_length=100)
	city_town=models.CharField(max_length=100)
	country=models.CharField(max_length=100)

	def __str__(self):
		return f' Profile for {self.user.username} '