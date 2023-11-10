from django.shortcuts import render
from .models import Curso, CategoriaCurso

# Create your views here.

def cursos(request):

    cursos=Curso.objects.all()

    return render(request, "cursos/cursos.html", {"cursos": cursos})

def exito(request):

    
    return render(request, "cursos/exito.html", {"cursos": cursos})


def categoriacurso(request, categoriacurso_id):

    categoriacurso=CategoriaCurso.objects.get(id=categoriacurso_id)
    cursos=Curso.objects.filter(categoriascurso=categoriacurso)
    return render(request, "cursos/categoriacurso.html", {'categoriacurso':categoriacurso,"cursos": cursos })