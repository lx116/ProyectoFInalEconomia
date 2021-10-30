from django.urls import path
from .views import renderHome

urlpatterns =[
    path('',renderHome,name='home')
]