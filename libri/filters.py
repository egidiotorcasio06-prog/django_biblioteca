import django_filters
from .models import Libro

class LibroFilter(django_filters.FilterSet):
    
    titolo = django_filters.CharFilter(lookup_expr='icontains', label='Cerca per Titolo')
    
    
    autore = django_filters.ModelChoiceFilter(queryset=Libro.objects.values_list('autore__cognome', flat=True).distinct(), label='Filtra per Autore')
    
    
    prezzo_min = django_filters.NumberFilter(field_name='prezzo', lookup_expr='gte', label='Prezzo Minimo')
    prezzo_max = django_filters.NumberFilter(field_name='prezzo', lookup_expr='lte', label='Prezzo Massimo')

    class Meta:
        model = Libro
        fields = ['titolo', 'autore', 'prezzo_min', 'prezzo_max', 'anno_pubblicazione', 'categorie']