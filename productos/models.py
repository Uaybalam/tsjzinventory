from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    grupo = models.TextField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    
    
    
