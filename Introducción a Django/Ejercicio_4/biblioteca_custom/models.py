from django.db import models

# Create your models here.

class Autor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField()

    def __str__(self):
	    return str(self.nombre + ' ' + self.apellido)

class Libro(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    editorial = models.CharField(max_length=20)
    paginas = models.IntegerField()

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
	    return str(self.titulo + " | " + self.editorial)

class Ejemplar(models.Model):
    codigo = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=30)
    estado = models.BooleanField(default=False)

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(self.libro.titulo + " (Copia)")

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField(blank=True, null=True)
    documento = models.IntegerField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=35, default=None)

    def mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    mayor_edad.boolean = True
    mayor_edad.short_description = "Mayor de edad"

    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
	    return str(self.nombre + ' ' + self.apellido)