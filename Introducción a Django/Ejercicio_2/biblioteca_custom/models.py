from django.db import models

# Create your models here.

class Autores(models.Model):
    codigo = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)

class Libros(models.Model):
    codigo = models.AutoField(primary_key=True)

    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=20)
    paginas = models.IntegerField()

    id_autor = models.ForeignKey(Autores, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)

class Ejemplares(models.Model):
    codigo = models.AutoField(primary_key=True)

    localizacion = models.CharField(max_length=30)

    id_libro = models.ForeignKey(Libros, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)

class Usuarios(models.Model):
    codigo = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    id_ejemplar = models.ForeignKey(Ejemplares, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.nombre)
