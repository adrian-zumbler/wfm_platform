from django.db import models

class Organization(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255,blank=True)

	def __unicode__(self):
		return self.name