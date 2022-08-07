from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


def probando_template(request):
    with open("C:/Users/Asus/PycharmProjects/ProyectoDjango/templates/template1.html", "r") as f:
        plantilla = Template(f.read())
    context = Context()
    documento = plantilla.render(context)

    return HttpResponse(documento)


def saludo(request):
    # Logica de negocio
    now = datetime.now()
    return HttpResponse(f"<h1 style= color:blue; >Hola desde Django <hr> en coder en la fecha: {now}</h1>")

def mi_nombre(request, name):
    text_response = f"El nombre ingresado es <span style= color:red;>{name.title()}</span>"
    return HttpResponse(text_response)