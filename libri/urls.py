from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libri, name='lista_libri'),
    path('aggiungi/', views.aggiungi_libro, name='aggiungi_libro'),
    path('dettaglio/<int:pk>/', views.dettaglio_libro, name='dettaglio_libro'),
]
