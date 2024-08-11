from django.contrib import admin
from .models import Kategoriler, Markalar, Urunler, Etiketler
from django.utils.html import format_html
# Register your models here.

#admin.site.register(Kategoriler) #kategorileri admin paneline ekledim

class KategorilerAdmin(admin.ModelAdmin):
    list_display =  ['name', 'seo_title', 'seo_description','slug', 'is_active']
    search_fields = ['name', 'seo_title', 'seo_description','slug']
    list_filter = ['is_active']

admin.site.register(Kategoriler, KategorilerAdmin)

class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['name', 'seo_title', 'seo_description', 'is_active', 'image_tag']
    search_fields = ['is_active', 'seo_title', 'name']
    list_filter = ['is_active', 'name']


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Resim'  #kullanılan resmin sitede gözükmesi için bu fonksiyon kullanıldı

admin.site.register(Markalar, MarkalarAdmin)


class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['name', 'fiat', 'marka', 'indirimli_fiat', 'is_active', 'image_tag', 'tarih']
    search_fields = ['name', 'kategori', 'is_active', 'marka']
    list_filter = ['slug', 'seo_title', 'name']

    def image_tag(self, obj):
        if obj.resim:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.resim.url))
        return "-"

    image_tag.short_description = 'Resim'  # Admin panelinde bu başlık altında gözükecek


admin.site.register(Urunler, UrunlerAdmin)

admin.site.register(Etiketler)
