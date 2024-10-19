from django.db import models

# Create your models here.
class Division(models.Model):
	nombre = models.CharField(max_length=200)
	fotografia = models.ImageField(upload_to='imagenes/', default='imagen')

	def __str__(self):
		return self.nombre

class AreaTrabajo(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(default='')
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	#archivo = models.FileField(upload_to='documentos/', blank=True, null=True)

	def __str__(self):
		return self.titulo + ' - ' + self.division.nombre

class Documento(models.Model):
	area_trabajo = models.ForeignKey(AreaTrabajo, on_delete=models.CASCADE, related_name='documentos')
	documento = models.FileField(upload_to='documentos/')
	nombre_documento = models.CharField(max_length=1000)
	descripcion_documento = models.TextField(blank=True, null=True) 

	def __str__(self):
	    return self.nombre_documento
