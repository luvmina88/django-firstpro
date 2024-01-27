from django.urls import path, include
from dj_pr.views import main

urlpatterns = [
    path('', main, name='main'),
]
