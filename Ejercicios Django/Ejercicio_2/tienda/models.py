from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=25)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=25)
    comuna = models.IntegerField()

    def __str__(self):
        s_numero = str(self.numero)
        return str(self.calle + ' ' + s_numero)

class Telefono(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)



class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        s_rut = str(self.rut)
        return str(s_rut + ' | ' + self.nombre)

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=35)
    web = models.CharField(max_length=150, default="None", null=True, blank=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        s_rut = str(self.rut)
        return str(s_rut + ' | ' + self.nombre + ' (Prov.)')

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=25, default=None)

    def __str__(self):
        return str(self.descripcion)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    precio = models.IntegerField()
    s_precio = '$' + str(precio)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        s_id = str(self.id)
        return str(s_id  + ' ' + self.nombre)

class Detalle_Venta(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descuento = models.IntegerField()
    #monto final