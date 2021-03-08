from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    identidad = models.CharField(max_length=20, null=False, blank=False)

class Boleto(models.Model):
    trayecto = models.IntegerField()    
    fecha_de_compra = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

class Asiento(models.Model):
    numero = models.IntegerField() 
    boleto = models.OneToOneField(Boleto, null= False, blank= False, on_delete=models.CASCADE)

class Bus(models.Model):
    patente = models.CharField(max_length=10)
    chofer = models.ForeignKey(Usuario,  on_delete=models.CASCADE, null=False, blank=False)
    capacidad_maxima = models.IntegerField(default=10) 
    
class Terminal(models.Model):
    direccion = models.CharField(max_length=30) 
    comuna = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=25)

class Trayecto(models.Model):
    fecha = models.DateTimeField()
    origen =  models.ForeignKey(Terminal, null=False, blank=False, on_delete=models.CASCADE, related_name='Trayecto_origen')
    destino = models.ForeignKey(Terminal, null=False, blank=False, on_delete=models.CASCADE, related_name='Trayecto_destino')
    bus =  models.ForeignKey(Bus, on_delete=models.CASCADE,  null=False, blank=False)
    precio = models.FloatField()
    
