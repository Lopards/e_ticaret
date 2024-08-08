from django.contrib import admin
from.models import Kategoriler

# Register your models here.
class KategorilerAdmin(admin.ModelAdmin):
    list_display =  ['name', 'seo_title', 'seo_description','slug', 'is_active']
    search_fields = ['name', 'seo_title', 'seo_description','slug']
    list_filter = ['is_active']

admin.site.register(Kategoriler) #kategorileri admin paneline ekledim

class MarkalarAdmin(admin.ModelAdmin): # markalar adlı bölümü admin paneline ekledim
    list_display = ['name', 'seo_title', 'seo_description', 'is_active', 'image_tag']
    search_fields = ['is_active', 'seo_title', 'name']
    list_filter = ['is_active', 'name']


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Resim'  #kullanılan resmin sitede gözükmesi için bu fonksiyon kullanıldı

admin.site.register(Markalar, MarkalarAdmin)
