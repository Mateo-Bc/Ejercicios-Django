from django.contrib import admin
from .models import *

class Cliente_Admin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'telefono']
    list_display_links = ['rut', 'nombre']



class Producto_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'stock']
    fieldsets = (
        ('Descripcion',{
            'fields':('nombre', 'categoria')
        }),
        ('Variables',{
            'fields':('proveedor', 'precio', 'stock')
        })
    )



class Venta_Admin(admin.ModelAdmin):
    pass



class Proveedor_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'web']
    list_filter = ('nombre', 'rut')

# Register your models here.

admin.site.register(Direccion,)
admin.site.register(Telefono, )

admin.site.register(Cliente, Cliente_Admin)
admin.site.register(Proveedor, Proveedor_Admin)
admin.site.register(Categoria, )
admin.site.register(Producto, Producto_Admin)
admin.site.register(Venta, Venta_Admin)