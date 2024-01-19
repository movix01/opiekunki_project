from django.contrib import admin
from django.urls import path, include
from opiekunki_app.views import strona_domowa  # Importuj widok

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strona_domowa, name='strona_domowa'),  # Ustaw jako strona domowa
    path('opiekunki/', include('opiekunki_app.urls')),  # Zawartość aplikacji opiekunki
]
