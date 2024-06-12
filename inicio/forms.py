from django import forms
from inicio.models import Cliente, Domicilio , Vehiculo
from django.contrib.auth.hashers import check_password

class CrearFormularioCliente(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'edad', 'contraseña']

    def clean_contraseña(self):
        contraseña = self.cleaned_data['contraseña']
        if len(contraseña) < 8 or not any(char.isdigit() for char in contraseña) or not any(char.isalpha() for char in contraseña):
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres, incluyendo letras y números.')
        return contraseña

class CrearFormularioDomicilio(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ['calle', 'numero', 'ciudad', 'provincia', 'pais']
        
class BuscarClienteForm(forms.Form):
    nombre_cliente = forms.CharField(label='Nombre del Cliente')

    def clean_nombre_cliente(self):
        nombre_cliente = self.cleaned_data['nombre_cliente']
        return nombre_cliente    
    
class BuscarVehiculoForm(forms.Form):
    marca = forms.CharField(label='Marca del Vehículo', max_length=100)    

class LoginForm(forms.Form):
    nombre_cliente = forms.CharField(label='Nombre del Cliente')
    contraseña = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        nombre_cliente = cleaned_data.get('nombre_cliente')
        contraseña = cleaned_data.get('contraseña')

        if nombre_cliente and contraseña:
            try:
                cliente = Cliente.objects.get(nombre=nombre_cliente)
                if not check_password(contraseña, cliente.contraseña):
                    self.add_error('contraseña', 'Contraseña incorrecta')
            except Cliente.DoesNotExist:
                self.add_error('nombre_cliente', 'Cliente no encontrado')
        return cleaned_data
    
        

        
