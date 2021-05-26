from django.urls import path
from . import views

urlpatterns = [
    path('', views.gameHome),
    path('clearGame', views.clearGame),
    path('setup_game',views.setup_game),
    path('game',views.game),
    path('process_game',views.process_game),
    path('results',views.results),
    path('splitOdds',views.splitOdds), 
]