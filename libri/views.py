from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def lista_libri(request):
    tutti_i_libri = Libro.objects.all()
    context = {
        'elenco_libri' : tutti_i_libri,
        'titolo_pagina' : 'Catalogo Completo Libri'
    }
    return render(request, 'libri/lista_libri.html', context)

def aggiungi_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libri')
    else:
        form = LibroForm()

    context = {
        'form': form,
        'titolo_pagina': 'Aggiungi un Nuovo Libro'
    }
    return render(request, 'libri/aggiungi_libro.html', context)



# Create your views here.
