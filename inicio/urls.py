from django.urls import path
from inicio import views
urlpatterns = [
    path('', views.inicio, name=inicio),
    path('template1/<str:nombre>/<str:apellido>', views.template1),
    path('template2/<str:nombre>/<str:apellido>', views.template2),
    path('template3/<str:nombre>/<str:apellido>', views.template3),
    path('template4/<str:nombre>/<str:apellido>', views.template4),
    path('probando', views.probando, name=probando),
    path('autos/crear/', views.crear_Vehiculo)
]
