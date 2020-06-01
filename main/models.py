from django.db import models
from django.utils import timezone



class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	tutorial_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural= "Categories"

	def __str__(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural= "Series"

	def __str__(self):
		return self.tutorial_series

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField(default = timezone.now())

	tutorial_series = models.ForeignKey(TutorialSeries, verbose_name="Series", default=1, on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.tutorial_title

class Blog(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField(default = timezone.now())


	def __str__(self):
		return self.title
# Create your models here.
