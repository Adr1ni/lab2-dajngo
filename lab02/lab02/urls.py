from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('encuesta/', include('encuesta.urls')),
    path('calculadora/', include('calculadora.urls')),
    path('volumen/',include('volumen.urls')),
]
