from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization
from tags.models import Tag
from agents.models import Agent

class Task(models.Model):
	statusOptions = {
		('Aplicada','Aplicada'),
		('Pendiente','Pendiente'),
		('Rechazada','Rechazada'),
	}
	date_published = models.DateField()
	status = models.CharField(max_length=255,choices=statusOptions)
	user = models.ForeignKey(User)
	orgzanization = models.ForeignKey(Organization)
	tag = models.ManyToManyField(Tag)
	agent = models.ForeignKey(Agent)

class File(models.Model):
	document = models.FileField(upload_to='files')
	task = models.ForeignKey(Task)

class Comment(models.Model):
	text = models.TextField()
	task = models.ForeignKey(Task)
	user = models.ForeignKey(User)	





