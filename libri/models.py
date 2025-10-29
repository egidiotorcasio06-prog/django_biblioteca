from django.db import models

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=100)
    anno_pubblicazione = models.IntegerField()
    descrizione = models.TextField()

    def __str__(self):
        return self.titolo

# Create your models here.
