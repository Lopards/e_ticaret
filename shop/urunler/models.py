from django.db import models

# Create your models here.
class Kategoriler(models.Model):
    name = models.CharField(max_length=50) #text alanı oluşturur
    is_active = models.BooleanField(default=True)#kategorinin aktif mi değil mi

    class Meta:
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"
    def __str__(self): # kategoriyi sitede göstermek için
        return self.name
