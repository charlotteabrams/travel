from django.shortcuts import render, redirect
from ..loginRegister.models import User
from .models import Travel
from django.db import models
from django.contrib import messages
from django.core.urlresolvers import reverse

def new(request):
    if "id" not in request.session:
        return redirect("my_login_index")

    return render(request, "blackbeltTemp/create.html")

def join(request, id):
    if "id" not in request.session:
        return redirect("my_login_index")
    
    trip = Travel.objects.get(id=id)
    user = User.objects.get(id=request.session["id"])

    trip.travellers.add(user)

    return redirect("my_login_home")

def create(request):
    print request.POST
    if request.method != 'POST':
        return redirect('create_trip')
    data = {
        "user": User.objects.get(id=request.session["id"])
    }
    results = Travel.travelManager.isValidAdd(request.POST, data)
    if results[0]:
        return redirect(reverse('my_login_home'))
    else: 
        errors = results[1]
        for error in errors:
            messages.error(request, error)
        return redirect(reverse('add_travel'))

def show(request, id):
    if "id" not in request.session:
        return redirect("my_login_index")
    context = {
        "trip": Travel.objects.get(id=id)
    }
    return render(request, "blackbeltTemp/show.html", context)





