from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    #render login page
    return render(request, 'index.html')

def success(request):
    #render successful login page w. user_name
    context = {
        "user": User.objects.get(email = request.session['email'])
    }
    return render(request, 'success.html', context)

def register(request):
    errors = User.objects.registration_validator(request.POST)
    print("*******errors: ", errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #if no errors, create user in db & redirect to '/success'
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email= request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())

    request.session['email'] = request.POST['email']
    return redirect('/success')

def login(request):
    #run validator
    errors = User.objects.login_validator(request.POST)
    #if errors, redirect to '/' w. error message
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #else, start session & redirect to '/success'
    request.session['email'] = request.POST['email']
    print("*********post request: ",request.POST)
    return redirect('/success')

def logout(request):
    #clear session
    request.session.clear()
    #redirect to index.html
    return redirect('/')