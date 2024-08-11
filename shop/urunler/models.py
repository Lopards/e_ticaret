from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Kategoriler(models.Model):
    name = models.CharField(max_length=50) #text alanı oluşturur
    is_active = models.BooleanField(default=True)#kategorinin aktif mi değil mi

    ust_kategori = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,
                    help_text="Eğer bu kategori başka bir kategoriye bağlıysa burayı doldurunuz.")

    seo_title = models.CharField(max_length=155,blank=True,null=True,help_text="e ticaretke")
    seo_description = models.TextField(blank=True,null=True,help_text="django e ticaret")
    slug = models.SlugField(blank=True,null=True,unique=True, help_text="")

    #image = models.ImageField(upload_to='D:\masaustu\Desktop\indir.jpg')
    class Meta:
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"
    def __str__(self):
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
            return self.name


class Etiketler(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(blank=True,null=True,unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Etiketler"
        verbose_name = "Etiket"

    def __str__(self):
        return self.name

class Urunler(models.Model):
    kullanici = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,help_text="")
    marka = models.ForeignKey(Markalar,on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='urunresimleri')
    tarih =models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=155)
    kategori = models.ForeignKey(Kategoriler, on_delete=models.CASCADE, blank=True,null=True)
    aciklama = models.TextField(blank=True,null=True)
    seo_title = models.CharField(max_length=155,blank=True,null=True)
    seo_description = models.TextField(blank=True,max_length=122)


    fiat = models.DecimalField(max_digits=10,decimal_places=2)
    kisa_aciklama = models.TextField(blank=True,null=True)
    indirimli_fiat = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    slug = models.SlugField(blank=True,null=True,unique=True)
    is_active = models.BooleanField(default=True)
    etiketler = models.ManyToManyField(Etiketler,blank=True) #



    class Meta:
        verbose_name_plural = "Urunler"
        verbose_name = "Urun"
    def __str__(self):
            return self.name
