from django.urls import path

from . import views

app_name = "aperitivos"

urlpatterns = [
    path('<slug:slug>', views.video, name='video'),
    path('', views.indice, name='indice'),
]
