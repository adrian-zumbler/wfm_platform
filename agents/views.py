from django.shortcuts import render,redirect
from .models import Agent
from organization.models import Organization
from django.contrib.auth.models import User
from django.conf import settings

def index(request):
	if not request.user.is_authenticated():
		return redirect('%s?next%s' % (settings.LOGIN_URL,request.path))
	user_id = request.user.id	
	user = User.objects.get(pk=user_id)
	if request.method == 'POST':
		name = request.POST['nameAgent']
		status = request.POST['status']
		organization = request.POST['organization']
		if name == "":
			agents = Agent.objects.filter(organization_id=organization).filter(status=status)
		else:
			agents = Agent.objects.filter(last_name__icontains=name).filter(organization_id=organization).filter(status=status)
	else:
		agents = __getAllAgents()
	organizations = Organization.objects.all()
	return render(request,'agents/index.html',{
		'agents':agents,
		'organizations':organizations,
		'user':user})


#return all Agents in the database whitout filter
def __getAllAgents():
	return Agent.objects.all()
#return all Organization in the database whitout filter
def __getAllOrganization():
	return Organization.objects.all()
#Return the actual auth user only when this is active






