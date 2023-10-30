from django.urls import path
from Guessing_game_App import views

urlpatterns = [
    path('',views.Home),
    path('entry',views.entry),
    path('gamewelcome',views.gamewelcome),
    path('gamecheck',views.gamecheck)
 
]
'''   '''