from django.urls import path

from . import views

urlpatterns = [
    path('', views.officialZoo),
    path('theZoos/', views.allZoos),
    path('createZoo/', views.createZoo),
#     path('animals/', views.animals),
#     path('addNew/', views.addAnimal),
#     path('create/', views.create),
]