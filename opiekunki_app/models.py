from django.db import models

class Opiekunka(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    opis = models.TextField()
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
