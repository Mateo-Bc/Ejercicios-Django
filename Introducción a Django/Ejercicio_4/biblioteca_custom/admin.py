from django.contrib import admin
from .models import *

#@admin.register(Libro) <- es lo mismo que -> admin.site.register(Libro)

class Libro_Admin(admin.ModelAdmin):
    exclude = ['codigo']
    list_display = ['titulo', 'editorial']
    #list_display_links = ['editorial']
    #list_editable = ('titulo',)

class LibroInline(admin.TabularInline):
    model = Libro

class Usuario_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'mayor_edad', 'direccion']
    list_display_links = ['nombre', 'apellido']
    fieldsets = (
	    ('Datos',{
	        'fields':('nombre', 'apellido', 'edad', 'documento')
	    }),
	    ('Contacto',{
	        'fields':('telefono', 'direccion')
	    }),
        ('Servicio',{
            'fields':('ejemplar',)
        })
    )

class Autor_Admin(admin.ModelAdmin):
    inlines = [LibroInline,]
    search_fields = ['nombre']

class Ejemplar_Admin(admin.ModelAdmin):
    list_display = ['libro', 'estado']
    list_filter = ('libro',)

# Register your models here.

admin.site.register(Autor, Autor_Admin)
admin.site.register(Libro, Libro_Admin)
admin.site.register(Ejemplar, Ejemplar_Admin)
admin.site.register(Usuario, Usuario_Admin)