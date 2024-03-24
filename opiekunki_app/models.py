from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Opiekunka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    plec = models.ForeignKey('Plec', on_delete=models.CASCADE)
    wiek = models.IntegerField(default=50)
    miasto = models.CharField(max_length=100)
    rodzaj = models.ForeignKey('Rodzaj', on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add=True)
    opis = models.TextField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    
class Plec(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa
    
class Rodzaj(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa
    
class Opinia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tresc = models.TextField()
    ocena = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    opiekunka = models.ForeignKey(Opiekunka, on_delete=models.CASCADE)

