from django.shortcuts import render

from pypro.base.models import Imagens


def home(request):
    img = Imagens()
    template_name = 'base/index.html'
    context = {
        'test_model_instance': img
    }
    return render(request, template_name, context)
