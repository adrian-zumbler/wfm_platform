from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User

def index(request):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
	user = User.objects.get(pk=request.user.id)	
	return render(request,'tasks/index.html',{'user':user})
