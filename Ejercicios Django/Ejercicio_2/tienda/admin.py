from django.contrib import admin
from .models import *

class Cliente_Admin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'telefono']
    list_display_links = ['rut', 'nombre']
    search_fields = ['nombre', 'rut']



class Producto_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'precio']
    fieldsets = (
        ('Descripcion',{
            'fields':('nombre', 'categoria')
        }),
        ('Variables',{
            'fields':('proveedor', 'precio', 'stock')
        })
    )



class Venta_Admin(admin.ModelAdmin):
    exclude = ['monto_total']
    readonly_fields = ['monto_final']
    list_display = ['id', 'cliente' , 'fecha', 'apl_desc', 'monto_final']
    list_display_links = ['id', 'cliente']
    fieldsets = (
        ('Información', {
            'fields':('fecha', 'cliente')
        }),
        ('Factura', {
            'fields':('producto', 'cantidad', 'monto_final', 'apl_desc', 'descuento')
        })
    )
    actions = ['disable_discounts', 'enable_discounts']

    def disable_discounts(self, request, queryset):
        return queryset.update(apl_desc = False)
    disable_discounts.short_description = 'Ignorar descuentos'

    def enable_discounts(self, request, queryset):
        return queryset.update(apl_desc = True)
    enable_discounts.short_description = 'Aplicar descuentos'



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