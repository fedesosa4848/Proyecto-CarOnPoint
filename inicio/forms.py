from django import forms
from inicio.models import Vehiculo, Auto, Moto, Camion, Camioneta
from django.contrib.auth.hashers import check_password

class FormularioVehiculo(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    combustible = forms.CharField(max_length=20)
    ano_fabricacion = forms.IntegerField(required=False, min_value=1980)
    imagen = forms.ImageField(required=False)  # Nuevo campo

class BuscarVehiculoForm(forms.Form):
    marca = forms.CharField(label='Marca del Vehículo', max_length=100, required=False)
    modelo = forms.CharField(label='Modelo del Vehículo', max_length=100, required=False)
    combustible = forms.CharField(label='Combustible del Vehículo', max_length=100, required=False)
    ano_fabricacion = forms.IntegerField(label='Año de Fabricación', required=False)

class FormularioAuto(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'combustible', 'ano_fabricacion', 'numero_puertas', 'imagen']

class FormularioMoto(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['marca', 'modelo', 'combustible', 'ano_fabricacion', 'tipo_manillar', 'imagen']

class FormularioCamion(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['marca', 'modelo', 'combustible', 'ano_fabricacion', 'capacidad_carga', 'imagen']

class FormularioCamioneta(forms.ModelForm):
    class Meta:
        model = Camioneta
        fields = ['marca', 'modelo', 'combustible', 'ano_fabricacion', 'capacidad_pasajeros', 'imagen']


        
