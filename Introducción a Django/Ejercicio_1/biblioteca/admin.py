from django.contrib import admin
from biblioteca.models import Autores
from biblioteca.models import Libros
from biblioteca.models import Ejemplares
from biblioteca.models import Usuarios

# Register your models here.

admin.site.register(Autores,)
admin.site.register(Ejemplares,)
admin.site.register(Libros,)
admin.site.register(Usuarios,)
