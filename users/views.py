from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from users.forms import MiFormulario
def log(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario =AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
           username = formulario.cleaned_data.get('username')
           password = formulario.changed_data.get('password')
           
           user = authenticate(request,username= username, password = password)
           
           login(request,user)
           
           return redirect ('inicio')
           
    
    return render(request, 'users/login.html',{'formulario' : formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = MiFormulario()
        if formulario.is_valid:
            formulario.save()
            return redirect ('inicio')
        
    return render(request, 'users/registro.html',{'formulario' : formulario} )