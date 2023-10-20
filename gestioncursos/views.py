from django.shortcuts import render, HttpResponse
from aspirante.models import Aspirante
from carro.carro import Carro

# Create your views here.

def home(request):
    carro=Carro(request)

    return render(request, "Universidad3/home.html")





def aspirante(request):

    aspirantes=Aspirante.objects.all()
    return render(request, "Universidad3/aspirante.html", {"aspirantes": aspirantes})

