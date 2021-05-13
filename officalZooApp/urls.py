from django.urls import path

from . import views

urlpatterns = [
    path('', views.officialZoo),
    path('theZoos/', views.allZoos),
    path('createZoo/', views.createZoo),
    path('<int:zoo_id>/editZoo/', views.editZoo),
    path('<int:zoo_id>/updateZoo/', views.updateZoo),
    path('<int:zoo_id>/deleteZoo/', views.deleteZoo),
    path('theAnimals/', views.allAnimals),
    path('createAnimal/', views.createAnimal),
    path('<int:animal_id>/editAnimal/', views.editAnimal),
    path('<int:animal_id>/updateAnimal/', views.updateAnimal),
    path('<int:animal_id>/deleteAnimal/', views.deleteAnimal),
]