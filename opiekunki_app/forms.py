from django import forms
from .models import Opiekunka

class OpiekunkaForm(forms.ModelForm):
    class Meta:
        model = Opiekunka
        fields = ['imie', 'nazwisko', 'plec', 'wiek', 'miasto', 'rodzaj', 'user']

    def __init__(self, user, *args, **kwargs):
        super(OpiekunkaForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()

class OgloszeniaFilterForm(forms.Form):
    miasto = forms.CharField(label='Miasto', required=False)
    plec = forms.ChoiceField(label='Płeć', choices=(('', '---'), ('2', 'Kobieta'), ('1', 'Mężczyzna'), ('3', 'Inne')), required=False)
    rodzaj = forms.ChoiceField(label='Rodzaj', choices=(('', '---'), ('2', 'Opieka nad osobą starszą'), ('1', 'Opieka nad dzieckiem'), ('3', 'Opieka nad zwirzęciem'), ('4', 'Opieka nad osobą chorą')), required=False)