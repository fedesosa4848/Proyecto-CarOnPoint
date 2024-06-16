from django.contrib import admin
from inicio.models import Auto,Camion,Camioneta,Moto
# Register your models here.


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'combustible', 'ano_fabricacion')
    list_filter = ('combustible', 'ano_fabricacion')
    search_fields = ('marca', 'modelo')

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'combustible', 'ano_fabricacion')
    list_filter = ('combustible', 'ano_fabricacion')
    search_fields = ('marca', 'modelo')

@admin.register(Camioneta)
class CamionetaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'combustible', 'ano_fabricacion')
    list_filter = ('combustible', 'ano_fabricacion')
    search_fields = ('marca', 'modelo')

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'combustible', 'ano_fabricacion')
    list_filter = ('combustible', 'ano_fabricacion')
    search_fields = ('marca', 'modelo')