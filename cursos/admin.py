from django.contrib import admin
from .models import CategoriaCurso, Curso

# Register your models here.

class CategoriaCursoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class CursoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(CategoriaCurso, CategoriaCursoAdmin)

admin.site.register(Curso, CursoAdmin)