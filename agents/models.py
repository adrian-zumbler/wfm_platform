from django.db import models
from organization.models import Organization

class Agent(models.Model):
	
	statusOptions = {
		('Activo', 'activo'),
		('Baja', 'baja'),
	}

	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	status = models.CharField(max_length=255,choices=statusOptions)
	min_hours = models.IntegerField()
	max_hours = models.IntegerField()
	css_number = models.IntegerField()
	avaya_number = models.IntegerField()
	organization =  models.ForeignKey(Organization)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name




	


