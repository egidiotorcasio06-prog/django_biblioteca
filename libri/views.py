from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Count, F
from .models import Libro
from .forms import LibroForm

def lista_libri(request):
    tutti_i_libri = Libro.objects.all()
    statistiche = {}
    if lista_libri.exists():
        statistiche['totale_libri'] = lista_libri.count()
        statistiche['pagine_medie'] = lista_libri.exclude(numero_pagine__isnull=True).aggregate(
            Avg('numero_pagine')
        )['numero_pagine__avg']
        statistiche['libri_per_autore'] = lista_libri.values('autore').annotate(
            count=Count('autore')
        ).order_by('-count')[:3]
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

def dettaglio_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    context = {
        'libro' : libro,
        'titolo_pagina' : f'Dettaglio: {libro.titolo}'
    }
    return render(request, 'libri/dettaglio_libro.html', context)


# Create your views here.
