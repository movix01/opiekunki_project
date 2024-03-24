from django import forms
from .models import Opiekunka, Opinia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RejestracjaForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':"username",
            'type':"text",
            'class':"form-input",
            'placeholder':"login",
            'maxlength':"20",
            'minlength':"5"
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':"password1",
            'type':"password",
            'class':"form-input",
            'placeholder':"hasło",
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':"password2",
            'type':"text",
            'class':"form-input",
            'placeholder':"login",
        })

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class OpiekunkaForm(forms.ModelForm):
    class Meta:
        model = Opiekunka
        fields = ['imie', 'nazwisko', 'plec', 'wiek', 'miasto', 'rodzaj', 'user', 'opis']

    def __init__(self, user, *args, **kwargs):
        super(OpiekunkaForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()

class OgloszeniaFilterForm(forms.Form):
    miasto = forms.CharField(label='Miasto', required=False)
    plec = forms.ChoiceField(label='Płeć', choices=(('', '---'), ('2', 'Kobieta'), ('1', 'Mężczyzna'), ('3', 'Inne')), required=False)
    rodzaj = forms.ChoiceField(label='Rodzaj', choices=(('', '---'), ('2', 'Opieka nad osobą starszą'), ('1', 'Opieka nad dzieckiem'), ('3', 'Opieka nad zwirzęciem'), ('4', 'Opieka nad osobą chorą')), required=False)

class OpiniaForm(forms.ModelForm):
    class Meta:
        model = Opinia
        fields = ['tresc', 'ocena', 'opiekunka', 'user']

    def __init__(self, user, *args, **kwargs):
        super(OpiniaForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['opiekunka'].widget = forms.HiddenInput()