from django.urls import path
from Guessing_game_App import views
urlpatterns = [
    path('',views.home ),
    path('usernameentry',views.usernameentry),
    path('rangeentry',views.rangeentry),
    path('numberentry',views.numberentry),
    path('validate',views.validate),
    ]
    
