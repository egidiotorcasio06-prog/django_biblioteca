from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.cognome}'

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.ForeignKey(Autore,
        on_delete=models.CASCADE, 
        related_name='libri'
    )
    anno_pubblicazione = models.IntegerField()
    descrizione = models.TextField()
    prezzo = models.DecimalField(
        max_digits=6,      # Massimo 6 cifre totali
        decimal_places=2,  # 2 cifre dopo la virgola (es: 9999.99)
        verbose_name="Prezzo (€)",
        help_text="Prezzo del libro in euro",
        null=True,
        blank=True
    )
    data_acquisto = models.DateField(
        verbose_name="Data di acquisto",
        help_text="Quando è stato acquistato il libro",
        null=True,
        blank=True
    )
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True) # ISBN ha max 13 cifre ed è unico
    numero_pagine = models.IntegerField(null=True, blank=True)
    categorie = models.ManyToManyField(
        Categoria, 
        related_name='libri',
        blank=True 
    )
    copertina = models.ImageField(upload_to='copertine/', blank=True, null=True)
    
    def __str__(self):
        return self.titolo

class Meta:
        unique_together = ('nome', 'cognome') 
        ordering = ['cognome', 'nome'], ['-data_creazione']
        verbose_name_plural = "Categorie"

class Recensione(models.Model):
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE, 
        related_name='recensioni'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voto = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], 
        help_text="Voto da 1 a 5 stelle"
    )
    commento = models.TextField(blank=True, null=True)
    data_creazione = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return f'Recensione per {self.libro.titolo} ({self.voto}/5)'

    
    



    
# Create your models here.
