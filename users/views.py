from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from users.forms import MiFormulario,EditarPerfil
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from users.models import DataUserExtra
from django.contrib.auth.models import User

from .forms import EditarAboutMeForm
from .models import DataUserExtra


def log(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            # Autenticación del usuario
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Iniciar sesión si la autenticación es exitosa
                login(request, user)
                
                DataUserExtra.objects.get_or_create(user=user)
                
                return redirect('inicio')  # Redirigir a la página de inicio
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = MiFormulario()

    return render(request, 'registro.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    try:
        datauserextra = request.user.datauserextra
    except DataUserExtra.DoesNotExist:
        # Crear el DataUserExtra si no existe
        datauserextra = DataUserExtra.objects.create(user=request.user)

    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            request.user.email = formulario.cleaned_data.get('email')
            request.user.first_name = formulario.cleaned_data.get('first_name')
            request.user.last_name = formulario.cleaned_data.get('last_name')
            request.user.save()

            datauserextra.avatar = formulario.cleaned_data.get('avatar')
            datauserextra.save()

            return redirect('editar_perfil')
    else:
        formulario = EditarPerfil(instance=request.user)

    return render(request, 'editar_perfil.html', {'formulario': formulario})


class CambiarPass(PasswordChangeView):
    template_name = 'cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
@login_required
def listar_perfiles(request):
    perfiles = DataUserExtra.objects.all()
    return render(request, 'listar_perfiles.html', {'perfiles': perfiles})

@login_required
def perfil_usuario(request):
    user = request.user
    user_extra = DataUserExtra.objects.get(user=user)
    return render(request, 'perfil_usuario.html', {'user': user, 'user_extra': user_extra})

def ver_perfil(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)
    return render(request, 'ver_perfil.html', {'usuario': usuario})

@login_required
def perfil_usuario(request):
    try:
        datauserextra = request.user.datauserextra
    except DataUserExtra.DoesNotExist:
        datauserextra = DataUserExtra.objects.create(user=request.user)

    if request.method == 'POST':
        form = EditarAboutMeForm(request.POST, instance=datauserextra)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = EditarAboutMeForm(instance=datauserextra)

    return render(request, 'perfil_usuario.html', {'form': form, 'datauserextra': datauserextra})
