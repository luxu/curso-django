from django.shortcuts import render, redirect

from .forms import PhotoForm
from .models import Photo


def home(request):
    template_name = 'base/index.html'
    context = {
        'imgs': Photo.objects.all()
    }
    return render(request, template_name, context)


def upload(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'base/upload.html', context)


def edit(request, id):
    context = dict(backend_form=PhotoForm())
    # photo = Photo.objects.filter(id=id)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'base/upload.html', context)
