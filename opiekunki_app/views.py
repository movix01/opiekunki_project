from django.shortcuts import render, redirect
from .models import Opiekunka
from .forms import OpiekunkaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def strona_domowa(request):
    context = {}
    if request.user.is_authenticated:
        # Jeśli użytkownik jest zalogowany
        pass  # Możesz tutaj dodać dodatkową logikę dla zalogowanych użytkowników
    else:
        # Jeśli użytkownik nie jest zalogowany
        context['show_login_register'] = True

    return render(request, 'opiekunki_app/strona_domowa.html', context)

@login_required
def lista_opiekunek(request):
    opiekunki = Opiekunka.objects.filter(user=request.user)
    return render(request, 'opiekunki_app/lista.html', {'opiekunki': opiekunki})

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
    return render(request, 'opiekunki_app/rejestracja.html', {'form': form})

def logowanie(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('strona_domowa')
    else:
        form = AuthenticationForm()
    return render(request, 'opiekunki_app/logowanie.html', {'form': form})

def wylogowanie(request):
    logout(request)
    return redirect('strona_domowa')