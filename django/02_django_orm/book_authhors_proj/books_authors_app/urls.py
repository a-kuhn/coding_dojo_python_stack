from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.book_profile),
    path('add_author_to_book', views.add_author_to_book),
    path('authors', views.authors_index),
    path('add_author', views.add_author),
    path('authors/<int:author_id>', views.author_profile),
    path('add_book_to_author', views.add_book_to_author),
]