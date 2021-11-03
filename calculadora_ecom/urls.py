from django.urls import path
from .views import renderHome,anualidadVencida__VP,anualidadVencida__VP_A,anualidadVencida__VP_N

urlpatterns =[
    path('',renderHome,name='home'),
    path('anualidadVencida__VP/',anualidadVencida__VP,name='Anualidad Vencida VP'),
    path('anualidadVencida__VP_A/',anualidadVencida__VP_A,name='Anualidad Vencida VP A'),
    path('anualidadVencida__VP_N/',anualidadVencida__VP_N,name='Anualidad Vencida VP N'),

]