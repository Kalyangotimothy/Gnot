from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="home_page"),
    path('addnotes/', views.addnotes, name="addnotes"),
    path('viewnote/<int:id>/', views.viewnote, name="viewnotes"),
]