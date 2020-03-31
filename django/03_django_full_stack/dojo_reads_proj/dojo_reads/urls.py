from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('books/add', views.add_book),
    path('books/<int:book_id>', views.book_profile),
    path('users/<int:user_id>', views.user),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('new_book', views.new_book),
    path('new_review', views.new_review),
    path('delete', views.delete),
]
