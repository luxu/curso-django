from django.urls import path

from .views import upload

urlpatterns = [
    path('/create', upload, name='create'),
    # path('', upload, name='photo_album'),
]
