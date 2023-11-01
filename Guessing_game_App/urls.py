from django.urls import path
from Guessing_game_App import views
urlpatterns = [
    path('',views.home ),
    path('guess',views.guess ),
    path('number',views.number ),
    path('validate',views.validate ),
    path('retry',views.retry ),
    path('validateretry',views.validateretry ),
]
