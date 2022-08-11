from django.db import models

# Create your models here.

class Bloger(models.Model):
    isim=models.CharField(max_length=120)
    soy_isim=models.CharField(max_length=120)
    biyografi = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.isim} {self.soy_isim}'



class Blog(models.Model):
    yazar = models.ForeignKey(Bloger,
                              on_delete=models.CASCADE,
                              related_name='blog')

class Blogger(models.Model):
    isim=models.CharField(max_length=122)
    soyIsim=models.CharField(max_length=122)

class Blog(models.Model):
    yazar = models.ForeignKey(Blogger, on_delete=models.CASCADE)

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