from django.urls import path
from . import views

url_patterns = [
    path('',views.match_rosters_view, name='match_rosters'),
]