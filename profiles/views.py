from django.shortcuts import render
from django.contrib.auth.models import User

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