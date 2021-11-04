from django.urls import path
from .views import renderHome,anualidadVencida__VP,anualidadVencida__VP_A,anualidadVencida__VP_N,anualidadVencida__VF,anualidadAnticipada__VP,anualidadAnticipada__VF,anualidadVencida__VF_A,anualidadAnticipada__A_VF,anualidadAnticipada__A


urlpatterns =[
    path('',renderHome,name='home'),
    path('anualidadVencida__VP/',anualidadVencida__VP,name='Anualidad Vencida VP'),
    path('anualidadVencida__VP_A/',anualidadVencida__VP_A,name='Anualidad Vencida VP A'),
    path('anualidadVencida__VP_N/',anualidadVencida__VP_N,name='Anualidad Vencida VP N'),
    path('anualidadVencida__VF/',anualidadVencida__VF,name='Anualidad Vencida VF'),
    path('anualidadAnticipada__VP/',anualidadAnticipada__VP,name='Anualidad Anticipada VP'),
    path('anualidadAnticipada__VF/',anualidadAnticipada__VF,name='Anualidad Anticipada VF'),
    path('anualidadAnticipada__VF_A/',anualidadVencida__VF_A,name='Anualidad Anticipada VF A'),
    path('anualidadAnticipada__VP_A',anualidadAnticipada__A, name='anualidad anticipada VP A'),
]