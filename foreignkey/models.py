from django.db import models

class Category(models.Model):
	class Meta:
		# change name on admin
		verbose_name_plural = 'categories'

	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=32)
	description = models.TextField()
	# we're going to link specific items to specific category
	category = models.ForeignKey(Category, on_delete=models.CASCADE,)

	def __str__(self):
		return self.name