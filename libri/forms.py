from django import forms 
from .models import Libro, Autore, Categoria, Recensione

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titolo', 'autore', 'anno_pubblicazione', 'descrizione', 'prezzo', 'data_acquisto', 'isbn', 'numero_pagine', 'copertina']
        labels = {
            'anno_pubblicazione' : 'Anno di Pubblicazione',
            'data_acquisto': 'Data di Acquisto (AAAA-MM-GG)',
            'numero_pagine': 'Numero di Pagine',
        }

class RecensioneForm(forms.ModelForm):
    class Meta:
        model = Recensione
        # Includiamo solo i campi che l'utente deve compilare: voto e commento
        fields = ['voto', 'commento']
        
        # Puoi usare i widgets per migliorare l'input, ad esempio per il voto
        widgets = {
            'voto': forms.NumberInput(attrs={'min': 1, 'max': 5, 'placeholder': 'Voto (1-5)'}),
            'commento': forms.Textarea(attrs={'rows': 4}),
        }       