from django.urls import path
from . import views

urlpatterns = [
    path('match-rosters/', views.match_rosters, name='match_rosters'),
]
