from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from users.forms import MiFormulario

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