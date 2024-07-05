from django.urls import path,include
from inicio import views
from django.conf import settings
from django.conf.urls.static import static


# si tiene el hashtag es funciones que estan si estas logeado, asi que, REGISTRATE ! :)
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about-us/', views.about_me, name='about-us'),
    path('crear/', views.seleccionar_tipo_vehiculo, name='seleccionar_tipo_vehiculo'), #
    path('crear/', views.crear_vehiculo, name='crear_vehiculo_main'), #
    path('autos/crear/', views.crear_auto, name='crear_auto'), #
    path('motos/crear/', views.crear_moto, name='crear_moto'), #
    path('camiones/crear/', views.crear_camion, name='crear_camion'),  #
    path('camionetas/crear/', views.crear_camioneta, name='crear_camioneta'), #
    path('catalogo/', views.catalogo_sin_login, name='catalogo'), 
    path('catalogo-vehiculos/', views.catalogo_vehiculos, name='catalogo-vehiculos'), # 
    path('buscar_vehiculo/', views.buscar_vehiculo, name='buscar_vehiculo'), #
    path('buscar_vehiculo_sin_log/', views.buscar_vehiculo_sinLogin, name='buscar_vehiculo_sin_log'),
    path('creacion-exitosa/<int:vehiculo_id>/<str:tipo>/', views.creacion_exitosa, name='creacion_exitosa'), #
    path('vehiculos/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'), #
    path('editar-vehiculo/<str:tipo>/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'), #
    path('ver-detalle/<str:tipo>/<int:id>/', views.ver_detalle_vehiculo, name='ver_detalle_vehiculo'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

