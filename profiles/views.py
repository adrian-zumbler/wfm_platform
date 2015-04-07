from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def index(request):
	profiles = User.objects.all()
	autorizado = ' No Acceso';
	if request.user.is_authenticated:
		autorizado = 'Acceso';
		email = request.user.profile.avatar.url
	else:
		autorizado = 'No Acceso'
	return render(request,'profiles/index.html',
		{'profiles': profiles,
		 'aut': autorizado,
		 'email': email
		 }
		)

def autentication(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/tasks/')
			else:
				pass
		else:
			return render_to_response('profiles/autentication.html',{"errorMessage": "El usuario o contasena son incorrectos"},context_instance=RequestContext(request))			
	return render(request,'profiles/autentication.html')			


		