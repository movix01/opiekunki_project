from django.urls import path
from . import views

urlpatterns = [
    path('', views.strona_domowa, name='strona_domowa'),
    path('lista_opiekunek/',views.lista_opiekunek, name='lista_opiekunek'),
    path('dodaj/', views.dodaj_opiekunke, name='dodaj_opiekunke'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('logowanie/', views.logowanie, name='logowanie'),
    path('wylogowanie/', views.wylogowanie, name='wylogowanie'),
    
]
