from django.urls import path
from .views import renderHome,anualidades_Variables,anualiadades_Uniformes


urlpatterns =[
    path('',renderHome,name='home'),
    path('anualidades_uniformes/',anualiadades_Uniformes,name='anualidades unifomres'),
    path('anualidades_Variables/',anualidades_Variables,name='Anualidades variables')
]