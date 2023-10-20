from django.shortcuts import render
from conocenos.models import Post, Categoria
# Create your views here.

def conocenos(request):
    posts=Post.objects.all()

    return render(request, "Conocenos/conocenos.html", {"post": posts})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    post=Post.objects.filter(categoria=categoria)
    return render(request, "blog/categoria.html", {'categorias': categoria,"post": post})