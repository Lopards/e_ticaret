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

class Markalar(models.Model):
    name = models.CharField(max_length=155)
    aciklama = models.TextField(blank=True,null=True,help_text="")
    seo_title = models.CharField(max_length=155,blank=True,null=True)
    seo_description = models.TextField(blank=True)
    slug = models.SlugField(blank=True,null=True,unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='markaresimleri')

    class Meta:
        verbose_name_plural = "Markalar"
        verbose_name = "Marka"

        def __str__(self):
            return self.verbose_name_plural
