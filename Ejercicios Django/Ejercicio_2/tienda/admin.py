from django.contrib import admin
from .models import *



# Register your models here.

admin.site.register(Direccion,)
admin.site.register(Telefono, )

admin.site.register(Cliente, )
admin.site.register(Proveedor, )
admin.site.register(Categoria, )
admin.site.register(Producto, )
admin.site.register(Detalle_Venta, )
admin.site.register(Venta, )