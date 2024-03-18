from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.strona_domowa, name='strona_domowa'),
    path('lista_opiekunek/',views.lista_opiekunek, name='lista_opiekunek'),
    path('dodaj/', views.dodaj_opiekunke, name='dodaj_opiekunke'),
    path('edytuj/<int:opiekunka_id>/', views.edytuj_opiekunke, name='edytuj_opiekunke'),
    path('usun/<int:opiekunka_id>/', views.usun_opiekunke, name='usun_opiekunke'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('logowanie/', views.logowanie, name='logowanie'),
    path('wylogowanie/', views.wylogowanie, name='wylogowanie'),
    path('ogloszenia/', views.ogloszenia, name='ogloszenia'),
    path('opinie_opiekunki/<int:opiekunka_id>/', views.opinie_opiekunki, name='opinie_opiekunki'),
    path('dodaj_opinie/<int:opiekunka_id>/', views.dodaj_opinie, name='dodaj_opinie'),
    path('edytuj_opinie/<int:opinia_id>/', views.edytuj_opinie, name='edytuj_opinie'),
    path('usun_opinie/<int:opinia_id>/', views.usun_opinie, name='usun_opinie'),
]

urlpatterns += staticfiles_urlpatterns()