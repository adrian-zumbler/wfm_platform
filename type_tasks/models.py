from django.db import models

class TypeTasks(models.Model):
	nombre = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

	


