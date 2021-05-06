from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('jquery/', views.jquery),
    path('skills/', views.skills),
    path('addSkill/', views.addSkill),
]
