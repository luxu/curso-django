from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from pypro.base.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
