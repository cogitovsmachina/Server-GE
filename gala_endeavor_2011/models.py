from django.db import models

class Alive (models.Model):
	alive = models.BooleanField()

class Productos(models.Model):
	id_prod =  models.IntegerField(primary_key = True)
	nombre  = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=4096)
	costo_inicial = models.DecimalField(max_digits=11, decimal_places=2, null= True)
	costo_actual = models.DecimalField(max_digits=11, decimal_places=2, null= True)
	costo_final = models.DecimalField(max_digits=11, decimal_places=2, null= True)
	last_bidder = models.ForeignKey('Usuarios', null= True)
	
class Usuarios (models.Model):
	user = models.CharField(max_length=50,primary_key = True)
	nombre = models.CharField(max_length=200)
	mesa =  models.IntegerField()
	tiempo_creacion = models.DateTimeField (auto_now=True)
	
class Tabletas (models.Model):
	id = models.IntegerField(primary_key = True)
	device = models.CharField(max_length=30)
	
	
class Pujas (models.Model):
	producto = models.ForeignKey('Productos')
	usuario = models.ForeignKey('Usuarios')
	precio_actual = models.DecimalField(max_digits=11, decimal_places=2)
	tiempo = models.DateTimeField (auto_now=True)
	
	 
