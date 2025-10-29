from django import forms 
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titolo', 'autore', 'anno_pubblicazione', 'descrizione']
        labels = {
            'anno_pubblicazione' : 'Anno di Pubblicazione'
        }