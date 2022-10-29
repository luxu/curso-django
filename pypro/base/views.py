from django.shortcuts import render

from pypro.modulos.models import Modulo


def home(request):
    template_name = 'base/home.html'
    modulos = Modulo.objects.all()
    context = {
        'MODULOS': modulos
    }
    return render(request, template_name, context)
