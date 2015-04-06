from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
				return render(request,'profiles/index.html')
	return render(request,'profiles/autentication.html')			


		