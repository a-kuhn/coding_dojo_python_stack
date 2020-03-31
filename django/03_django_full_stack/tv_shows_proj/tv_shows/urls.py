from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_all),
    path('shows', views.display_all),
    path('shows/new', views.add_new),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.display_one),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/update/<int:show_id>', views.update),
    path('shows/destroy/<int:show_id>', views.destroy),
]