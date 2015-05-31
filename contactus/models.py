from django.db import models

# Create your models here.

class Supporter(models.Model):
	name=models.CharField(max_length=100)
	