from django.urls import path,include
from inicio import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about-us/', views.about_me, name='about-us'),
    path('crear/', views.seleccionar_tipo_vehiculo, name='seleccionar_tipo_vehiculo'),
    path('crear/', views.crear_vehiculo, name='crear_vehiculo_main'),
    path('autos/crear/', views.crear_auto, name='crear_auto'), #Solo
    path('motos/crear/', views.crear_moto, name='crear_moto'), #Funciona
    path('camiones/crear/', views.crear_camion, name='crear_camion'), #Logeado
    path('camionetas/crear/', views.crear_camioneta, name='crear_camioneta'), #Asi que
    path('catalogo-vehiculos/', views.catalogo_vehiculos, name='catalogo-vehiculos'), #Registrate :)
    path('buscar_vehiculo/', views.buscar_vehiculo, name='buscar_vehiculo'),
    path('creacion-exitosa/<int:vehiculo_id>/<str:tipo>/', views.creacion_exitosa, name='creacion_exitosa'), #Este tmb
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
