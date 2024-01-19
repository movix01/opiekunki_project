from django import forms
from .models import Opiekunka

class OpiekunkaForm(forms.ModelForm):
    class Meta:
        model = Opiekunka
        fields = ['imie', 'nazwisko', 'opis', 'user']

    def __init__(self, user, *args, **kwargs):
        super(OpiekunkaForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()