from django import forms
from .models import Opiekunka

class OpiekunkaForm(forms.ModelForm):
    class Meta:
        model = Opiekunka
        fields = ['imie', 'nazwisko', 'opis']
