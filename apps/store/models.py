from django.db import models

class Product(models.Model):

	title = models.CharField(max_length=255)
	slug 	= models.SlugField(max_length=255)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField()

	def __str__(self):
	  return self.title