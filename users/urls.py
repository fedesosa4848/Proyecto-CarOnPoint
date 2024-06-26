from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login', views.log, name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('SignIn', views.registro, name='SignIn'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('CambiarPass', views.CambiarPass.as_view(), name='CambiarPass'),
    path('perfiles/', views.listar_perfiles, name='listar_perfiles'),
]
