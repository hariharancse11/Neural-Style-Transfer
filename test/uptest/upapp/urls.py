# your_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books, name='get_books'),
    path('<int:pk>/', views.get_book, name='get_book'),
    path('create/', views.create_book, name='create_book'),
    path('<int:pk>/update/', views.update_book, name='update_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
]
