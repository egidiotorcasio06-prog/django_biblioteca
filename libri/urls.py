from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libri, name='lista_libri'),
    path('aggiungi/', views.aggiungi_libro, name='aggiungi_libro'),
    path('dettaglio/<int:pk>/', views.dettaglio_libro, name='dettaglio_libro'),
    path('modifica/<int:pk>/', views.modifica_libro, name='modifica_libro'),
    path('elimina/<int:pk>/', views.elimina_libro, name='elimina_libro')
]
