from django.db import models
from django.contrib.auth.models import User

class Opiekunka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    plec = models.ForeignKey('Plec', on_delete=models.CASCADE)
    wiek = models.IntegerField(default=50)
    miasto = models.CharField(max_length=100)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    
class Plec(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa