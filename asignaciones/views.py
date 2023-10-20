from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from flask import redirect
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags 
from django.core.mail import send_mail

from asignaciones.models import Asignacion, LineaAsignacion

# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_asignacion(request):
    asignacion=Asignacion.objects.create(user=request.user)
    carro=Carro(request)
    lineas_asignacion=list()
    for key, value in carro.carro.items():
        lineas_asignacion.append(LineaAsignacion(
            curso_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            asignacion=asignacion 
        ))

    LineaAsignacion.objects.bulk_create(lineas_asignacion)

    enviar_mail(
        asignacion=asignacion,
        lineas_asignacion=lineas_asignacion,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, "La asignación de curso fue exitosa")

    return redirect('../cursos')

def enviar_mail(**kwargs):

    asunto="La asignación de cursos fue Exitosa"
    mensaje=render_to_string("emails/asignacion.html",{
        "asignacion": kwargs.get("asignacion"),
        "lineas_asignacion": kwargs.get("lineas_asignacion"),
        "nombreusuario": kwargs.get("nombreusuario")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="masteruserpaiz@gmail.com"
    to=kwargs.get("emailusuario")
    #to="dorianchuquiej@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)