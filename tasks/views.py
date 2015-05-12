from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from .models import Task
from .models import File
from .models import Comment

def index(request):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))	
	user = User.objects.get(pk=request.user.id)
	name = user.first_name + ' ' + user.last_name
	tasks = Task.objects.all()
	
	return render(request,'tasks/index.html',{'user':user,'name': name,'tasks':tasks})

def view(request,id):
	task = Task.objects.get(id=id)
	files = File.objects.filter(task_id=task.id)
	comments = Comment.objects.filter(task_id=task.id)
	return render(request,'tasks/view.html',{'task':task,'files':files,'comments':comments})
