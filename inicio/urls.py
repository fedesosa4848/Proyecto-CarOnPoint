from django.urls import path,include
from inicio import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo-vehiculos', views.catalogo_vehiculos, name='catalogo-vehiculos'),
    path('autos/crear/', views.crear_auto_v2, name='crear'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
