
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('book_for/<int:id>', book_for, name="book_for"),
]
