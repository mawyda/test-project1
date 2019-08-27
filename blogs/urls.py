# blogs/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    # Create
    path('create/', views.create, name = 'create'),
    # Read
    path('<int:blog_id>/', views.details, name = 'details'),
    # Update
    path('update/<int:blog_id>/', views.update, name = 'update'),
    # Delete
    path('delete/<int:blog_id>/', views.delete, name = 'delete'),

]
