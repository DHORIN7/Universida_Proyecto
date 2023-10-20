from django.db import models

# Create your models here.

class CategoriaCurso(models.Model):
    nombre=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaCurso'
        verbose_name_plural='categoriasCurso'

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaCurso, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='cursos', null=True, blank=True)
    creditos=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'

    def __str__(self):
        return self.nombre
