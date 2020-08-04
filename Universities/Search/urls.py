from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    url(r'^getUniversities/', views.getUniversity, name="getUniversity"),
    url(r'^createUniversity/', views.createUniversity, name="createniversity"),
    path('updateUniversity/<int:pk>/', views.updateUniversity, name="updateUniversity"),
    path('deleteUniversity/<int:pk>/', views.deleteUniversity, name="deleteUniversity"),
    path('searchUniversity/', views.searchUniversity.as_view()),

]
