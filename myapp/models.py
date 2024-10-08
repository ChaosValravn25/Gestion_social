from django.db import models

# Create your models here.
class Division(models.Model):
	nombre = models.CharField(max_length=200)
	fotografia = models.ImageField(upload_to='imagenes/', default='imagen')

	def __str__(self):
		return self.nombre

class AreaTrabajo(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=2000)
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	archivo = models.FileField(upload_to='documentos/', blank=True, null=True)

	def __str__(self):
		return self.titulo + ' - ' + self.division.nombre
