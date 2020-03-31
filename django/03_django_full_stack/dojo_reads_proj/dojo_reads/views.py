from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import *

# Create your views here.
# ? RENDER FUNCTIONS
def index(request):
    #renders login/reg 
    return render(request, 'index.html')

def books(request):
    #renders all books homepage
    context = {
        "user": User.objects.get(email = request.session['email']),
        "books": Book.objects.all(),
        "reviews": Review.objects.all().order_by("-created_at")[:3],
    }
    return render(request, 'books.html', context)

def add_book(request):
    #renders the add book & review page
    context = {
        "authors": Author.objects.all().order_by("name"),
    }
    return render(request, 'add_book.html', context)

def book_profile(request, book_id):
    #renders the individual book profile page
    context = {
        "user": User.objects.get(email = request.session['email']),
        "book": Book.objects.get(id = book_id),
        "books": Book.objects.all(),
        "reviews": Review.objects.filter(book_id = book_id).order_by("-created_at")[:3],
    }
    print(context)
    return render(request, 'book_profile.html', context)

def user(request, user_id):
    #renders the individual user's info
    reviewed_books = Review.objects.filter(user_id = user_id)
    context = {
        "user": User.objects.get(id = int(user_id)),
        "reviewed_books": reviewed_books,
        "num_of_reviews": len(reviewed_books),
    }
    return render(request, 'user.html', context)

# ? REDIRECT FUNCTIONS
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
        name = request.POST['name'],
        alias = request.POST['alias'],
        dob = request.POST['dob'],
        email = request.POST['email'],
        password = bcrypt.hashpw((request.POST['password']).encode(), bcrypt.gensalt()).decode(),
    )
    request.session['email'] = request.POST['email']
    print("creating new user...")
    return redirect('/books')

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
    return redirect('/books')

def logout(request):
    #clear session 
    request.session.clear()
    #redirect to index
    return redirect('/')

def new_book(request):
    print("new_book post request: ", request.POST)
    #adds book to db, redirects to book's profile page
    errors = Book.objects.new_book_validator(request.POST)
    errors.update(Review.objects.review_validator(request.POST))
    if request.POST['new_author'] != '':
        errors.update(Author.objects.new_author_validator(request.POST))
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/add')

    if request.POST['new_author'] != '':
        new_author = Author.objects.create(name= request.POST['new_author'])
        Book.objects.create(title = request.POST['title'], author_id= new_author.id)
    else:
        Book.objects.create(
            title = request.POST['title'],
            author_id = Author.objects.get(name = request.POST['author']).id,
        )
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        user_id = User.objects.get(email = request.session['email']).id,
        book_id = Book.objects.get(title = request.POST['title']).id,
    )
    return redirect('books/'+str(Book.objects.get(title = request.POST['title']).id))


def new_review(request):
    #adds new review to db, redirects to book's profile page
    print("new review post request: ", request.POST)
    print("session : ", request.session['email'])
    errors = Review.objects.review_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/'+str(request.POST['book_id']))

    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        user_id = User.objects.get(email = request.session['email']).id,
        book_id = request.POST['book_id'],
    )
    return redirect('/books/'+str(request.POST['book_id']))

def delete(request):
    print("delete button post request: ",request.POST)
    #deletes review, redirects to book's profile page
    Review.objects.get(id = request.POST['delete_review']).delete()
    return redirect('/books')