from django.shortcuts import render, redirect, get_object_or_404
from .models import Opiekunka, Opinia
from .forms import OpiekunkaForm, OgloszeniaFilterForm, OpiniaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def strona_domowa(request):
    context = {}
    if request.user.is_authenticated:
        # Jeśli użytkownik jest zalogowany
        pass  # Możesz tutaj dodać dodatkową logikę dla zalogowanych użytkowników
    else:
        # Jeśli użytkownik nie jest zalogowany
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/strona_domowa.html', context)

def ogloszenia(request):
    opiekunki = Opiekunka.objects.all()
    form = OgloszeniaFilterForm(request.GET)

    if form.is_valid():
        miasto = form.cleaned_data.get('miasto')
        plec = form.cleaned_data.get('plec')
        rodzaj = form.cleaned_data.get('rodzaj')
        
        if miasto:
            opiekunki = opiekunki.filter(miasto__icontains=miasto)
        
        if plec:
            opiekunki = opiekunki.filter(plec=plec)

        if rodzaj:
            opiekunki = opiekunki.filter(rodzaj=rodzaj)

    context = {'opiekunki': opiekunki,
               'form': form,
               'show_login_register': False}

    if request.user.is_authenticated:
        pass 
    else:
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/ogloszenia.html', context)

def opinie_opiekunki(request, opiekunka_id):
    opiekunka = get_object_or_404(Opiekunka, pk=opiekunka_id)
    opinie = Opinia.objects.filter(opiekunka=opiekunka)
    context = {'opiekunka': opiekunka,
               'opinie': opinie,
               'show_login_register': False}
    if request.user.is_authenticated:
        pass 
    else:
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/opinie_opiekunki.html', context)

def dodaj_opinie(request, opiekunka_id):
    opiekunka = get_object_or_404(Opiekunka, id=opiekunka_id)
    if request.method == 'POST':
        form = OpiniaForm(request.user, request.POST)
        if form.is_valid():
            opinia = form.save(commit=False)
            opinia.opiekunka = opiekunka
            opinia.save()
            return redirect('opinie_opiekunki', opiekunka_id=opiekunka_id)
    else:
        form = OpiniaForm()
    context = {'form': form,
               'show_login_register': False}
    
    if request.user.is_authenticated:
        pass 
    else:
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/dodaj_opinie.html', context)

@login_required
def lista_opiekunek(request):
    opiekunki = Opiekunka.objects.filter(user=request.user)
    context = {'opiekunki': opiekunki,
               'show_login_register': False}
    if request.user.is_authenticated:
        pass 
    else:
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/lista.html', context)

@login_required
def dodaj_opiekunke(request):
    if request.method == 'POST':
        form = OpiekunkaForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_opiekunek')
    else:
        form = OpiekunkaForm(request.user)
    return render(request, 'opiekunki_app/dodaj.html', {'form': form})

@login_required
def edytuj_opiekunke(request, opiekunka_id):
    opiekunka = get_object_or_404(Opiekunka, id=opiekunka_id, user=request.user)
    if request.method == 'POST':
        form = OpiekunkaForm(request.user, request.POST, instance=opiekunka)
        if form.is_valid():
            form.save()
            return redirect('lista_opiekunek')
    else:
        form = OpiekunkaForm(request.user, instance=opiekunka)
    return render(request, 'opiekunki_app/edytuj.html', {'form': form, 'opiekunka': opiekunka})

@login_required
def usun_opiekunke(request, opiekunka_id):
    opiekunka = get_object_or_404(Opiekunka, id=opiekunka_id, user=request.user)
    if request.method == 'POST':
        opiekunka.delete()
        return redirect('lista_opiekunek')
    return render(request, 'opiekunki_app/usun.html', {'opiekunka': opiekunka})

def rejestracja(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('strona_domowa')
    else:
        form = UserCreationForm()
    context = { 'form': form,
               'show_login_register': False}
    if request.user.is_authenticated:
        pass 
    else:
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/rejestracja.html', context)

def logowanie(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('strona_domowa')
    else:
        form = AuthenticationForm()
    context = { 'form': form,
               'show_login_register': False}
    if request.user.is_authenticated:
        pass 
    else:
        context['show_login_register'] = True
    return render(request, 'opiekunki_app/logowanie.html', context)

def wylogowanie(request):
    logout(request)
    return redirect('strona_domowa')