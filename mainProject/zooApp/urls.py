from django.urls import path

from . import views

urlpatterns = [
    path('', views.zoo),
    path('form/', views.form),
    path('add-new/', views.newMembers),
    path('results/', views.results),
    path('the-shop/', views.theShop),
    path('reset/', views.reset),
    path('purchase/', views.purchase)
]
