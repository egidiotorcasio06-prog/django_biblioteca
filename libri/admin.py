from django.contrib import admin
from .models import Libro, Autore, Categoria, Recensione

admin.site.register(Libro)
admin.site.register(Autore)
admin.site.register(Categoria)
admin.site.register(Recensione)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'anno_pubblicazione', 'prezzo', 'get_categorie', 'media_voti')
    list_filter = ('autore', 'categorie', 'anno_pubblicazione')
    search_fields = ('titolo', 'autore__cognome', 'isbn')
    filter_horizontal = ('categorie')

    def media_voti(self, obj):
        media = obj.recensioni.aggregate(admin.models.Avg('voto'))['voto__avg']
        return f'{media:.2f}' if media else 'N/D'
    def get_categorie(self, obj):
        return ", ".join([c.nome for c in obj.categorie.all()])
    get_categorie.short_description = 'Categorie'

admin.site.register(Libro, LibroAdmin)

