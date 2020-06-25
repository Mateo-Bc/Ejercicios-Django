from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=25)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=25)
    comuna = models.IntegerField()

    def __str__(self):
        return str(self.calle + ' ' + self.numero)

class Telefono(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)



class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    #telefono
    #direccion

    def __str__(self):
        return str(self.rut + ' | ' + self.nombre)

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=35)
    web = models.CharField(max_length=150)
    #telefono
    #direccion

    def __str__(self):
        return str(self.rut + ' | ' + self.nombre + '(Prov.)')

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descricion = models.CharField

    def __str__(self):
        return str(self.descricion)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    precio = models.IntegerField()
    stock = models.IntegerField()
    #proveedor

    def __str__(self):
        return str(self.id + ' ' + self.nombre)

class Detalle_Venta(models.Model):
    cantidad = models.IntegerField()
    #producto

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descuento = models.IntegerField()
    #monto final