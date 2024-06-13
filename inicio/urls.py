from django.urls import path,include
from inicio import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio_logueado/', views.inicio_logueado, name='inicio_logueado'),
    path('sign-in', views.crear_cliente, name='sign-in'),
    path('about-us',views.about_me, name='about-us'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('autos/crear/', views.crear_auto_v2, name='crear'),
    path('catalogo-vehiculos', views.catalogo_vehiculos, name='catalogo-vehiculos'),
    path('catalogo_vehiculos_logged', views.catalogo_vehiculos_logged, name= 'catalogo_vehiculos_logged'),
    path('buscar_vehiculo/', views.buscar_vehiculo, name='buscar_vehiculo'),
    path('ver-clientes/', views.ver_clientes, name='ver_clientes'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
