from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login',views.log,name='login'),
    path('logout', LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('SignIn',views.registro,name='SignIn'),

]
