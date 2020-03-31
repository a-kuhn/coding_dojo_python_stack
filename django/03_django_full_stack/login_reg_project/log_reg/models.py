from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}
        #email in db already
        if len(User.objects.filter(email = post_data['email']))>0:
            errors['email'] = "Email already registered"
            return errors
        #check email format using regex
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        # pw == pw_confirm
        if post_data['pw_confirm'] != post_data['password']:
            errors['pw_confirm'] = "Password does not match"
        #len(first_name)
        if len(post_data['first_name'])<2:
            errors['first_name'] = "first name too short"
        #len(last_name)
        if len(post_data['last_name'])<2:
            errors['last_name'] = "last name too short"
        #len(password)
        if len(post_data['password'])<2:
            errors['password'] = "Password too short"
        return errors


    def login_validator(self, post_data):
        errors = {}
        #email in db
        if len(User.objects.filter(email=post_data['email'])) == 0:
            errors['email'] = 'That email is not registered.'
        #correct pw
        if not bcrypt.checkpw(post_data['password'].encode(), User.objects.filter(email = post_data['email'])[0].password.encode()):
            errors['password'] = "That password doesn't work."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()