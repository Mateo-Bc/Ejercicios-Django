from django.contrib import admin
#from biblioteca_custom.models import Autores
from .models import *

class Usuario_Admin(admin.ModelAdmin):
    exclude = ['codigo']

    fieldsets = (
	('informacion_personal',{
	    'fields':('nombre', 'direccion', 'telefono')
	}),
	('detalles del pedido',{
	    'fields':('id_ejemplar',)
	})
    )

    list_display = ['nombre', 'telefono', 'direccion']

# Register your models here.
admin.site.register(Autores,)
admin.site.register(Ejemplares,)
admin.site.register(Libros,)
admin.site.register(Usuarios,Usuario_Admin)
