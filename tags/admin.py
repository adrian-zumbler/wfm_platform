from django.contrib import admin
from .models import Tag

class AdminTag(admin.ModelAdmin):
	pass
admin.site.register(Tag,AdminTag)	
