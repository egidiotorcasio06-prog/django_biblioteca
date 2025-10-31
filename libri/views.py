from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Count, F
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Libro, Recensione
from .forms import RecensioneForm
from .forms import LibroForm
from .filters import LibroFilter

def lista_libri(request):
    tutti_i_libri = Libro.objects.all().order_by('titolo')
    page_number = request.Get.get('page')
    paginator = Paginator(lista_libri, 10)
    page_obj = paginator.get_page(page_number)
    paginator = Paginator(elenco_filtrato, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    libri_per_anno = Libro.objects.values('anno_pubblicazione').annotate(
        count=Count('pk')
    ).order_by('anno_pubblicazione')
    statistiche = {}
    if lista_libri.exists():
        statistiche['totale_libri'] = lista_libri.count()
        statistiche['pagine_medie'] = lista_libri.exclude(numero_pagine__isnull=True).aggregate(
            Avg('numero_pagine')
        )['numero_pagine__avg']
        statistiche['libri_per_autore'] = lista_libri.values('autore').annotate(
            count=Count('autore')
        ).order_by('-count')[:3]
        statistiche['chart_labels'] = [item['anno_pubblicazione'] for item in libri_per_anno]
    statistiche['chart_data'] = [item['count'] for item in libri_per_anno]
    libro_filter = LibroFilter(request.GET, queryset=lista_libri)
    elenco_filtrato = libro_filter.qs
    context = {
        'elenco_libri' : tutti_i_libri,
        'titolo_pagina' : 'Catalogo Completo Libri'
        'page_obj',
        'lista_libri' : page_obj.object_list,
        'titolo_pagina' : 'Catalogo Completo'
        'statistiche'
        'filter'  
    }
    return render(request, 'libri/lista_libri.html', context)
@login_required(redirect_field_name='next', login_url='/accounts/login/')
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

@login_required(redirect_field_name='next', login_url='/accounts/login/')
def dettaglio_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form_recensione = RecensioneForm(request.POST)
    if form_recensione.is_valid():
            nuova_recensione = form_recensione.save(commit=False)
            nuova_recensione.libro = libro
            nuova_recensione.user = request.user 
            nuova_recensione.save()
            return redirect('dettaglio_libro', pk=libro.pk)
    else:
        form_recensione = RecensioneForm()
    media_voti = libro.recensioni.aggregate(Avg('voto'))['voto__avg']
    context = {
        'libro' : libro,
        'titolo_pagina' : f'Dettaglio: {libro.titolo}',
        'media_voti': f'{media_voti:.2f}' if media_voti else 'N/D',
        'form_recensione' : form_recensione,
        'recensioni_esistenti': libro.recensioni.all()
    }
    return render(request, 'libri/dettaglio_libro.html', context)
def modifica_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('dettaglio_libro', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    context = {
        'form' : form,
        'libro' : libro,
        'titolo_pagina' : f'Modifica: {libro.titolo}'
    }
    return render(request, 'libri/modifica_lbro.html', context)
def elimina_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_lbri')
    context = {
        'libro' : libro,
        'titolo_pagina' : f'Conferma Eliminazione: {libro.titolo}'
    }
    return render(request, 'libri/elimina_libro.html', context)



# Create your views here.
