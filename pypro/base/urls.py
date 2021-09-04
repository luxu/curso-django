from django.urls import path

from pypro.base.views import home, trader, investy

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('trader/<str:country>/<str:stock>/', trader, name='trader'),
    path('trader/', investy, name='investy'),
]
