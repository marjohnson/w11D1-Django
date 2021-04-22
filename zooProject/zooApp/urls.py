from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contributors/', views.contributors),
    path('test/', views.test),
    path('form/', views.form),
    path('add-new/', views.newMembers),
    path('results/', views.results),
]
