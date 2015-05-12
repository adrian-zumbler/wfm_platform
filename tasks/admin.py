from django.contrib import admin
from .models import Task
from .models import File
from .models import Comment


class FileInline(admin.StackedInline):
	model = File
	can_delelte = False

class CommentInline(admin.StackedInline):
	model = Comment
	can_delelte = False

class TaskAdmin(admin.ModelAdmin):
	inlines = (FileInline,CommentInline,)


admin.site.register(Task,TaskAdmin)
