from django.db import models
from django.contrib.auth import get_user_model
from cursos.models import Curso
from django.db.models import F, Sum, FloatField
# Create your models here.

User=get_user_model()

class Asignacion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    
    
    @property
    def total(self):
        return self.lineaasignacion_set.aggregate(
            total=Sum(F("creditos")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)
    
    def __str__(self):
        return self.id


    class Meta:
        db_table='asignaciones'
        verbose_name='Asignacion'
        verbose_name_plural='Asignaciones'
        ordering=['id']

class LineaAsignacion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    asignacion=models.ForeignKey(Asignacion, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} asignación al curso de {self.curso.nombre}'
    
    class Meta:
        db_table='lineaasignaciones'
        verbose_name='Línea Asignacion'
        verbose_name_plural='Líneas Asignaciones'
        ordering=['id']

    

    
