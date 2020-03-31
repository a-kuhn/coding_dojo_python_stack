from django.db import models
from django.contrib import messages
import re
import bcrypt
from datetime import datetime

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, post_data):
        print("*****post_data: ", post_data)
        errors = {}
        #is email already in db?  --> yes = add message to errors, return errors
        potential_new_user = User.objects.filter(email = post_data['email'])
        if len(potential_new_user)>0:
            errors['not_new'] = "Email already registered"
            return errors
        #regex for email, len(first_name, last_name, password, pw==pw_confirm)
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['name'])<2:
            errors['name'] = "first name too short"
        if len(post_data['alias'])<2:
            errors['alias'] = "last name too short"
        if len(post_data['password'])<8:
            errors['password'] = "password too short"
        if post_data['password'] != post_data['pw_confirm']:
            errors['pw_match'] = "passwords do not match"
        if post_data['dob'] > datetime.now().strftime("%Y-%m-%d"):
            errors['dob'] = "invalid birthdate"
        #check if user is at least 13 yrs old     
        if int(datetime.now().strftime("%Y%m%d")) - int(re.sub('-', '', post_data['dob'])) <=130000:
            errors['dob'] = "sorry, you're too young!" 
        return errors

    def login_validator(self, post_data):
        errors = {}
        #is email in db?  --> no = add message to errors, return erros
        login_attempt = User.objects.filter(email = post_data['email'])
        if len(login_attempt)==0:
            errors['existing_email'] = "This email has not been registered"
            return errors
        #does pw match
        if not bcrypt.checkpw(post_data['password'].encode(), User.objects.filter(email = post_data['email'])[0].password.encode()):
            errors['password'] = "That password doesn't work."
        return errors
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    dob = models.DateTimeField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class AuthorManager(models.Manager):
    def new_author_validator(self, post_data):
        errors = {}
        #is author already in db?
        new_author = Author.objects.filter(name = post_data['new_author'])
        if len(new_author)!=0:
            errors['existing_author'] = "This author is already here-- double check the dropdown!"
        #name len
        if len(post_data['new_author'])<2:
            errors['name_length'] = "not a valid author"
        return errors
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class BookManager(models.Manager):
    def new_book_validator(self, post_data):
        errors = {}
        # is title already in db?
        new_title = Book.objects.filter(title = post_data['title'])
        if len(new_title)!=0:
            errors['title_exists'] = "This book is already here"
        # title len
        if len(post_data['title'])<2:
            errors['title_length'] = "not a valid title"
        return errors
class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)


class ReviewManager(models.Manager):
    def review_validator(self, post_data):
        errors = {}
        if len(post_data['content'])<10:
            errors['content'] = "Your review must be at least 10 characters."    
        return errors
class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
