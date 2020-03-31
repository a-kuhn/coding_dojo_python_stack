from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import *


# Create your views here.
def index(request):
    #renders login/reg 
    return render(request, 'index.html')

def wall(request):
    print("loading the wall...")
    #renders user's wall
    context = {
        "user": User.objects.get(email = request.session['email']),
        "users": User.objects.all(),
        "wall_messages": Message.objects.all().order_by("-created_at"),
        "comments": Comment.objects.all().order_by("created_at"),
    }
    return render(request, 'wall.html', context)

def register(request):
    #validate potential new user
    errors = User.objects.registration_validator(request.POST)
    #fail = redirect to index with messages
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #succeed = create user, add user to session **hash password**, redirect to success
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dob = request.POST['dob'],
        email = request.POST['email'],
        password = bcrypt.hashpw((request.POST['password']).encode(), bcrypt.gensalt()).decode(),
    )
    request.session['email'] = request.POST['email']
    print("creating new user...")
    return redirect('/wall')

def login(request):
    #validate login info: if email in db, if pw matches
    errors = User.objects.login_validator(request.POST)
    #fail = redirect to index with messages
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #succeed = redirect to user's wall 
    request.session['email'] = request.POST['email']
    print("logging in user...")
    return redirect('/wall')

def logout(request):
    #clear session 
    request.session.clear()
    #redirect to index
    return redirect('/')

def post_message(request):
    print("adding new message to db...", request.POST['post_message'])
    #add user's message to db
    Message.objects.create(
        m_content = request.POST['post_message'],
        user_id = User.objects.get(email=request.session['email']).id
    )
    #redirect to user's wall
    return redirect('/wall')

def post_comment(request):
    #add user's comment to db with link to correct message
    Comment.objects.create(
        c_content = request.POST['post_comment'],
        user_id = User.objects.get(email=request.session['email']).id,
        message_id= request.POST["msg_id"],
    )
    #redirect to user's wall
    return redirect('/wall')

def delete(request):
    # delete message if posted by current user
    print(request.POST)
    Message.objects.get(id=request.POST['msg_id']).delete()
    #redirect to wall
    return redirect('/wall')