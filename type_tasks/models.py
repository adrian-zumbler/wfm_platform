from django.db import models

class TypeTaks(models.Model):
	name = CharField(max_lenght=255)
	description = CharField(max_lenght=255)

