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
    path('theEmployees/', views.allEmployees),
    path('createEmployee/', views.createEmployee),
    path('<int:employee_id>/editEmployee/', views.editEmployee),
    path('<int:employee_id>/updateEmployee/', views.updateEmployee),
    path('<int:employee_id>/deleteEmployee/', views.deleteEmployee),
    path('theShows/', views.show),
    path('createShow/', views.createShow),
]