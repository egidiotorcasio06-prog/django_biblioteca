from django.db import models

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=100)
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

    def __str__(self):
        return self.titolo

# Create your models here.
