from django import forms 
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titolo', 'autore', 'anno_pubblicazione', 'descrizione', 'prezzo', 'data_acquisto', 'isbn', 'numero_pagine', 'copertina']
        labels = {
            'anno_pubblicazione' : 'Anno di Pubblicazione',
            'data_acquisto': 'Data di Acquisto (AAAA-MM-GG)',
            'numero_pagine': 'Numero di Pagine',
        }