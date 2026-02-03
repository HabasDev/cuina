from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.faqs, name='faqs'),
]
