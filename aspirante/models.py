from django.db import models

# Create your models here.

class Aspirante(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='aspirante')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='aspirante'
        verbose_name_plural='aspirantes'

    def __str__(self):
        return self.titulo