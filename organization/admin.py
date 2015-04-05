from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
	listFields = ('name','description')

admin.site.register(Organization,OrganizationAdmin)	

