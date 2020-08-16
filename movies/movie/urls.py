from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('movies/', views.movielist, name="movielist"),
    path('collections/', views.collection, name='collections'),
    path('collection/<str:uuid>', views.editCollection, name='collections'),
    path('request-count/', views.counter, name="counter"),
    path('request-count/reset/', views.resetcounter, name="resetcounter"),
    path('register/', views.Register.as_view()),
]
