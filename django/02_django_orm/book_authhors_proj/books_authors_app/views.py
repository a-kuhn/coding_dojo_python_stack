from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    #render page to add book
    print(request.POST)
    context = {
        "books": Book.objects.all(),
    }
    return render(request, 'index.html', context)

def add_book(request):
    #check for title already in db
    book_check = Book.objects.filter(title = request.POST["title"])
    if len(book_check)>0:
        return redirect('/')
    #grab input info and add to d
    else:
        Book.objects.create(title = request.POST["title"], desc = request.POST["desc"])
    return redirect('/')

def book_profile(request, book_id):
    #render page to display book profile
    context = {
        "book": Book.objects.get(id=book_id),
        "authors": Author.objects.all(),
    }
    return render(request, 'book_profile.html', context)

def add_author_to_book(request):
    #check if link already exists  ****NOT WORKING****
    print("***---post request: ",request.POST)
    author_to_add = Author.objects.get(id = request.POST['author'])
    print(author_to_add.first_name)
    authors_to_check = Book.objects.get(id=request.POST['book_id']).authors.filter(id=author_to_add.id).__dict__
    print("authors_to_check: ", authors_to_check)
    print("connected authors: ", Book.objects.get(id=request.POST['book_id']).authors.all().values())
    print("author_to_add: ", author_to_add)
    print(type(author_to_add)) #<class 'books_authors_app.models.Author'>
    print("book_id: ", request.POST['book_id'])
    
    #add connection to db
    Book.objects.get(id=request.POST['book_id']).authors.add(author_to_add)
    return redirect('/books/'+request.POST['book_id'])

def authors_index(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def add_author(request):
    author_check = Author.objects.filter(first_name = request.POST["First_name"], last_name = request.POST["Last_name"])
    if len(author_check)>0:
        return redirect('/')
    #grab input info and add to db
    else:
        Author.objects.create(first_name = request.POST["First_name"], last_name = request.POST["Last_name"], notes = request.POST["notes"])
    return redirect('/authors')


def author_profile(request, author_id):
    #render page with author
    context = {
        "author": Author.objects.get(id = author_id),
        "books": Book.objects.all()
    }
    return render(request, 'author_profile.html', context)

def add_book_to_author(request):
    # ****ADD A CHECK TO SEE IF CONNECTION ALREADY EXISTS****
    #make connection between 2 objects in db
    book_to_add = Book.objects.get(id = request.POST['book'])    
    Author.objects.get(id=request.POST['author']).books.add(book_to_add)
    return redirect('/authors/'+request.POST['author'])
