from django.db import models
from PIL import Image

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.imagen.path)
        
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.imagen.path)