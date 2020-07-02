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



class Categoria(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    descripcion = models.CharField(max_length=25, default=None)

    def __str__(self):
        return str(self.descripcion)



class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rut) + ' | ' + self.nombre



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre)


        
class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=35)
    web = models.CharField(max_length=150, default="None", null=True, blank=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.rut) + ' | ' + self.nombre + ' (Prov.)'



class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()

    apl_desc = models.BooleanField(default=False)
    descuento = models.IntegerField(default=None, blank=True, null=True)
    cantidad = models.IntegerField(default=None)
    monto_total = models.IntegerField(default=0, blank=True, null=True)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, default=None)

    def monto_final(self):
        if (self.apl_desc == True):
            return '$' + str(self.producto.precio * self.cantidad - self.descuento)
        else:
            return '$' + str(self.producto.precio * self.cantidad)
        self.monto_total = monto_final 
    monto_final.short_description = 'Monto total'
    apl_desc.short_description = 'Aplicar descuento'
    