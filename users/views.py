from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from users.forms import MiFormulario,EditarPerfil
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from users.models import DataUserExtra

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

    formulario = EditarPerfil(initial={'avatar': datauserextra.avatar}, instance=request.user)

    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            datauserextra.avatar = formulario.cleaned_data.get('avatar')
            datauserextra.save()

            formulario.save()
            return redirect('editar_perfil')

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