from django.db import models

class Organization(models.Modeln):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)