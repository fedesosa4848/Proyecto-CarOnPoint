from django import forms
from inicio.models import Cliente, Domicilio , Vehiculo

class CrearFormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'edad', 'domicilio']

class CrearFormularioDomicilio(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ['calle', 'numero', 'ciudad', 'provincia', 'pais']
