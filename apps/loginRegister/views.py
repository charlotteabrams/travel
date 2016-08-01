from django.shortcuts import render, redirect
from .models import User, UserManager
from ..blackbeltApp.models import Travel
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse

####################################################

# PROCESSING DATA 

####################################################

def processregister(request):
	if request.method != "POST":
		return redirect("my_login_index")
	results = User.userManager.isValidReg(request.POST)
	errors = results[1]
	for error in errors:
		messages.error(request, error)
	if results[0]:
		guy = User.objects.get(username = request.POST['username'])
		request.session['id'] = guy.id
		request.session['username'] = guy.username
		return redirect(reverse('my_login_home'))
	else: 
		return redirect(reverse('my_login_register'))

def processlogin(request):
	if request.method != "POST":
		return redirect("my_login_index")
	results = User.userManager.validlog(request.POST)
	if results[0]:
		request.session['id'] = results[1].id
		request.session['username'] = results[1].username
		return redirect(reverse('my_login_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.warning(request, error)
		return redirect(reverse('my_login_index'))





####################################################

# DISPLAY PAGES SECTION  

####################################################

def index(request):
	return render(request, 'travelAppTemplates/index.html')

def home(request):
	if "id" not in request.session:
		return redirect("my_login_index")

	user = User.objects.get(id=request.session["id"])
	context = {
		"trips_on": Travel.objects.filter(creator=user) | Travel.objects.filter(travellers__id=user.id),
		"trips_off": Travel.objects.exclude(creator=user).exclude(travellers__id=user.id),
		"name": user.name,
	}
	return render(request, 'travelAppTemplates/home.html', context)

def register(request):
	return render(request, 'travelAppTemplates/registration.html')

 
def logout(request):
	request.session.clear()
	return redirect(reverse('my_login_index'))

