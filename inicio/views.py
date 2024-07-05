from django.shortcuts import render,redirect,get_object_or_404
from inicio.models import Moto,Auto,Camion,Camioneta
from django.core.exceptions import ValidationError
from .forms import FormularioAuto, FormularioMoto, FormularioCamion, FormularioCamioneta,BuscarVehiculoForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#vista

def inicio(request):
    return render(request, 'inicio/index.html')

def about_me(request):
    return render(request, 'about_us.html')


# Vista para seleccionar el tipo de vehículo a crear
def seleccionar_tipo_vehiculo(request):
    return render(request, 'inicio/templatesCreacion/creacion_v2.html')

# Vista general para crear vehículos
@login_required
def crear_vehiculo(request, formulario_class, template_name):
    if request.method == 'POST':
        formulario = formulario_class(request.POST, request.FILES)  # Asegúrate de manejar los archivos
        if formulario.is_valid():
            datos_vehiculo = formulario.cleaned_data
            modelo = formulario_class.Meta.model
            if modelo.objects.filter(marca=datos_vehiculo.get('marca'), modelo=datos_vehiculo.get('modelo')).exists():
                return render(request, 'inicio/templates-resultadosVehiculos/vehiculo_ya_existe.html')
            else:
                try:
                    vehiculo = formulario.save(commit=False)
                    vehiculo.full_clean()  # Ejecuta las validaciones del modelo
                    vehiculo.save()
                    return redirect('creacion_exitosa', vehiculo.id, modelo.__name__.lower())
                except ValidationError as e:
                    formulario.add_error(None, e.message)  
        return render(request, template_name, {'formulario': formulario})
    else:
        formulario = formulario_class()
    return render(request, template_name, {'formulario': formulario})

# Vistas específicas para cada tipo de vehículo
def crear_auto(request):
    return crear_vehiculo(request, FormularioAuto, 'inicio/templatesVehiculos/crear_auto.html')

def crear_moto(request):
    return crear_vehiculo(request, FormularioMoto, 'inicio/templatesVehiculos/crear_moto.html')

def crear_camion(request):
    return crear_vehiculo(request, FormularioCamion, 'inicio/templatesVehiculos/crear_camion.html')

def crear_camioneta(request):
    return crear_vehiculo(request, FormularioCamioneta, 'inicio/templatesVehiculos/crear_camioneta.html')

def creacion_exitosa(request, vehiculo_id, tipo):
    try:
        if tipo == 'auto':
            vehiculo = Auto.objects.get(id=vehiculo_id)
        elif tipo == 'moto':
            vehiculo = Moto.objects.get(id=vehiculo_id)
        elif tipo == 'camion':
            vehiculo = Camion.objects.get(id=vehiculo_id)
        elif tipo == 'camioneta':
            vehiculo = Camioneta.objects.get(id=vehiculo_id)
        else:
            return render(request, 'inicio/templates-ResultadosVehiculo/error.html', {'mensaje': 'Tipo de vehículo no válido.'})

        return render(request, 'inicio/templatesCreacion/creacion_exitosa.html', {'vehiculo': vehiculo, 'tipo': tipo})
    except (Auto.DoesNotExist, Moto.DoesNotExist, Camion.DoesNotExist, Camioneta.DoesNotExist):
        raise Http404("El vehículo solicitado no existe en la base de datos.")

def catalogo_vehiculos(request):
    autos = Auto.objects.all()
    motos = Moto.objects.all()
    camiones = Camion.objects.all()
    camionetas = Camioneta.objects.all()
    return render(request, 'inicio/templatesCreacion/catalogo_vehiculos.html', {
        'autos': autos,
        'motos': motos,
        'camiones': camiones,
        'camionetas': camionetas
    })

def catalogo_sin_login(request):
    autos = Auto.objects.all()
    motos = Moto.objects.all()
    camiones = Camion.objects.all()
    camionetas = Camioneta.objects.all()
    return render(request, 'inicio/templates_sin_login/catalogo_sinLogin.html', {
        'autos': autos,
        'motos': motos,
        'camiones': camiones,
        'camionetas': camionetas
    })    

def ver_detalle_vehiculo(request, tipo, id):
    # Determinar el modelo adecuado según el tipo de vehículo
    if tipo == 'auto':
        vehiculo = get_object_or_404(Auto, id=id)
    elif tipo == 'moto':
        vehiculo = get_object_or_404(Moto, id=id)
    elif tipo == 'camion':
        vehiculo = get_object_or_404(Camion, id=id)
    elif tipo == 'camioneta':
        vehiculo = get_object_or_404(Camioneta, id=id)
    else:
        # Manejo de error si el tipo de vehículo no es válido
        return render(request, 'error.html', {'mensaje': 'Tipo de vehículo no válido'})

    # Contexto para pasar a la plantilla
    contexto = {
        'vehiculo': vehiculo,
        'tipo': tipo  # Pasamos el tipo de vehículo como contexto
    }

    return render(request, 'inicio/templates-resultadosVehiculos/ver_detalle_vehiculo.html', contexto)


def buscar_vehiculo(request):
    form = BuscarVehiculoForm(request.GET or None)
    vehiculos_encontrados = []

    if request.method == 'GET' and form.is_valid():
        # Obtener los datos del formulario
        marca = form.cleaned_data.get('marca')
        modelo = form.cleaned_data.get('modelo')
        combustible = form.cleaned_data.get('combustible')
        ano_fabricacion = form.cleaned_data.get('ano_fabricacion')

        # Crear un diccionario de filtros
        filtros = {}

        # Agregar filtros si los campos están completos
        if marca:
            filtros['marca__icontains'] = marca
        if modelo:
            filtros['modelo__icontains'] = modelo
        if combustible:
            filtros['combustible__icontains'] = combustible
        if ano_fabricacion:
            filtros['ano_fabricacion'] = ano_fabricacion

        # Filtrar sobre las subclases concretas solo si hay filtros aplicados
        if filtros:
            autos = Auto.objects.filter(**filtros)
            motos = Moto.objects.filter(**filtros)
            camiones = Camion.objects.filter(**filtros)
            camionetas = Camioneta.objects.filter(**filtros)

            vehiculos_encontrados = list(autos) + list(motos) + list(camiones) + list(camionetas)

    return render(request, 'inicio/templates-resultadosVehiculos/resultado_busqueda_vehiculo.html', {'form': form, 'vehiculos_encontrados': vehiculos_encontrados})


def buscar_vehiculo_sinLogin(request):
    form = BuscarVehiculoForm(request.GET or None)
    vehiculos_encontrados = []

    if request.method == 'GET' and form.is_valid():
        # Obtener los datos del formulario
        marca = form.cleaned_data.get('marca')
        modelo = form.cleaned_data.get('modelo')
        combustible = form.cleaned_data.get('combustible')
        ano_fabricacion = form.cleaned_data.get('ano_fabricacion')

        # Crear un diccionario de filtros
        filtros = {}

        # Agregar filtros si los campos están completos
        if marca:
            filtros['marca__icontains'] = marca
        if modelo:
            filtros['modelo__icontains'] = modelo
        if combustible:
            filtros['combustible__icontains'] = combustible
        if ano_fabricacion:
            filtros['ano_fabricacion'] = ano_fabricacion

        # Filtrar sobre las subclases concretas solo si hay filtros aplicados
        if filtros:
            autos = Auto.objects.filter(**filtros)
            motos = Moto.objects.filter(**filtros)
            camiones = Camion.objects.filter(**filtros)
            camionetas = Camioneta.objects.filter(**filtros)

            vehiculos_encontrados = list(autos) + list(motos) + list(camiones) + list(camionetas)

    return render(request, 'inicio/templates_sin_login/resultado_busqueda_sinlogin.html', {'form': form, 'vehiculos_encontrados': vehiculos_encontrados})

def eliminar_vehiculo(request, id):
    # Intenta encontrar el vehículo en cada subclase
    modelos = [Auto, Moto, Camion, Camioneta]
    vehiculo = None

    for modelo in modelos:
        try:
            vehiculo = modelo.objects.get(id=id)
            break
        except modelo.DoesNotExist:
            continue

    if vehiculo:
        vehiculo.delete()
    return redirect('catalogo-vehiculos')

def editar_vehiculo(request, tipo, id):
    # Determinar el modelo y formulario adecuado según el tipo de vehículo
    if tipo == 'auto':
        Vehiculo = Auto
        Formulario = FormularioAuto
    elif tipo == 'moto':
        Vehiculo = Moto
        Formulario = FormularioMoto
    elif tipo == 'camion':
        Vehiculo = Camion
        Formulario = FormularioCamion
    elif tipo == 'camioneta':
        Vehiculo = Camioneta
        Formulario = FormularioCamioneta
    else:
        # Manejo de error si el tipo de vehículo no es válido
        return render(request, 'error.html', {'mensaje': 'Tipo de vehículo no válido'})

    # Recuperar instancia del vehículo a editar
    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == 'POST':
        # Crear una instancia del formulario y asignar datos para guardar
        form = Formulario(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('catalogo-vehiculos')  # Redirigir al catálogo después de editar
    else:
        # Cargar formulario inicial con datos del vehículo a editar
        form = Formulario(instance=vehiculo)

    return render(request, 'inicio/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})
