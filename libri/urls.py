from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libri, name='lista_libri'),
    path('aggiungi/', views.aggiungi_libro, name='aggiungi_libro'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 0a5445e3f91971f729e8bbbeeaf306d323885f21
