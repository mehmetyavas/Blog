from django.db import models

# Create your models here.


class Blog(models.Model):
    yazar = models.CharField(max_length=150)
    baslik = models.CharField(max_length=150)
    aciklama = models.CharField(max_length=150)
    metin = models.TextField(max_length=150)
    sehir = models.CharField(max_length=150)
    yayinlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik