from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization

class Profile(models.Model):
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=255)
	avatar = models.ImageField(upload_to='media')
	organization = models.ForeignKey(Organization)



