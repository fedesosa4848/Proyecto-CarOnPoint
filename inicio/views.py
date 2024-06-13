from django.shortcuts import render,redirect
from .forms import CrearFormularioCliente, CrearFormularioDomicilio, BuscarClienteForm, BuscarVehiculoForm
from inicio.models import Vehiculo,Cliente
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .decorators import cliente_activo
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm



#vista

def inicio(request):
    return render(request, 'inicio/index.html')

def about_me(request):
    return render(request, 'about_us.html')

def inicio_logueado(request):
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        cliente = Cliente.objects.get(id=cliente_id)
        return render(request, 'inicio/index_logueado.html', {'cliente': cliente})
    else:
        return redirect('login')  # Redirigir al login si no hay cliente en la sesión


def crear_auto_v2(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        combustible = request.POST.get('combustible')
        ano_fabricacion = request.POST.get('ano_fabricacion')

        
        if marca and modelo:  # Verifica que se hayan proporcionado valores para la marca y el modelo
            if Vehiculo.objects.filter(marca=marca, modelo=modelo).exists():
                # Si el vehículo ya existe en la base de datos, redirige a una página de error
                return render(request, 'inicio/vehiculo_ya_existe.html')
            else:               
                try:
                    auto = Vehiculo(marca=marca, modelo=modelo, combustible=combustible, ano_fabricacion=ano_fabricacion)
                    auto.clean()  # Esto activará la validación definida en el modelo
                    auto.save()
                    return render(request, 'inicio/creacion_exitosa.html', {'auto': auto})
                except ValidationError as e:
                    error_message = e.message
                    return render(request, 'inicio/error.html', {'error_message': error_message})
    else:
        # Si la solicitud no es POST, simplemente renderiza la página de creación
        return render(request, 'inicio/creacion_v2.html')


def catalogo_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inicio/catalogo_vehiculos.html', {'vehiculos': vehiculos})

def catalogo_vehiculos_logged(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inicio/catalogo_logged.html', {'vehiculos': vehiculos})


def crear_cliente(request):
    if request.method == 'POST':
        cliente_form = CrearFormularioCliente(request.POST)
        domicilio_form = CrearFormularioDomicilio(request.POST)
        if cliente_form.is_valid() and domicilio_form.is_valid():
            domicilio = domicilio_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.domicilio = domicilio
            try:
                cliente.clean()
                cliente.save()
                # Guardar el cliente_id en la sesión
                request.session['cliente_id'] = cliente.id
                return redirect('inicio_logueado')  # Redirige a alguna vista después de crear el cliente
            except ValidationError as e:
                print("Error en la validación de cliente:", e.message)
                cliente_form.add_error('contraseña', e.message)  # Agregar error específico para la contraseña
                print("Formulario de cliente válido después de agregar error:", cliente_form.is_valid())
                cliente_form.is_valid()  # Validar explícitamente el formulario después de agregar el error
                print("Formulario de cliente válido después de validar explícitamente:", cliente_form.is_valid())
        else:
            # Retener los datos ingresados por el usuario en los campos válidos
            cliente_form.fields['nombre'].initial = request.POST.get('nombre')
            cliente_form.fields['apellido'].initial = request.POST.get('apellido')
            cliente_form.fields['edad'].initial = request.POST.get('edad')
            domicilio_form.fields['calle'].initial = request.POST.get('calle')
            domicilio_form.fields['numero'].initial = request.POST.get('numero')
            domicilio_form.fields['ciudad'].initial = request.POST.get('ciudad')
            domicilio_form.fields['provincia'].initial = request.POST.get('provincia')
            domicilio_form.fields['pais'].initial = request.POST.get('pais')
    else:
        cliente_form = CrearFormularioCliente()
        domicilio_form = CrearFormularioDomicilio()
    return render(request, 'crear_cliente.html', {'cliente_form': cliente_form, 'domicilio_form': domicilio_form})



from django.contrib.auth.hashers import check_password
def login_view(request):
    if request.method == 'POST':
        print("Solicitud POST recibida")
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre_cliente = form.cleaned_data['nombre_cliente']
            contraseña = form.cleaned_data['contraseña']

            # Mensajes de depuración
            print("Nombre del cliente recibido en el formulario:", nombre_cliente)
            print("Contraseña recibida en el formulario:", contraseña)

            try:
                cliente = Cliente.objects.get(nombre=nombre_cliente)

                # Mensaje de depuración
                print("Cliente encontrado en la base de datos:", cliente)

                if check_password(contraseña, cliente.contraseña):
                    # Contraseña correcta, establece la sesión del cliente
                    request.session['cliente_id'] = cliente.id
                    messages.success(request, 'Inicio de sesión exitoso.')
                    return redirect('inicio_logueado')
                else:
                    # Contraseña incorrecta
                    form.add_error('contraseña', 'Contraseña incorrecta')
            except Cliente.DoesNotExist:
                # Cliente no encontrado
                form.add_error('nombre_cliente', 'Cliente no encontrado')
    else:
        print("Solicitud GET recibida")
        form = LoginForm()
        
    print("Renderizando la plantilla 'login.html'")
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    if 'cliente_id' in request.session:
        del request.session['cliente_id']
        print("La sesión del cliente se ha eliminado correctamente.")
    else:
        print("La sesión del cliente no existe o ya ha sido eliminada.")
    return redirect('inicio')



def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'inicio/ver_clientes.html', {'clientes': clientes})

def buscar_cliente(request):
    if request.method == 'POST':
        form = BuscarClienteForm(request.POST)
        if form.is_valid():
            nombre_cliente = form.cleaned_data['nombre_cliente']
            clientes_encontrados = Cliente.objects.filter(nombre__icontains=nombre_cliente)
            return render(request, 'inicio/resultado_busqueda.html', {'clientes_encontrados': clientes_encontrados})
    else:
        form = BuscarClienteForm()
    return render(request, 'inicio/resultado_busqueda.html', {'form': form})

def buscar_vehiculo(request):
    if request.method == 'POST':
        form = BuscarVehiculoForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            vehiculos_encontrados = Vehiculo.objects.filter(marca__icontains=marca)
            return render(request, 'inicio/resultado_busqueda_vehiculo.html', {'vehiculos_encontrados': vehiculos_encontrados})
    else:
        form = BuscarVehiculoForm()
    return render(request, 'inicio/resultado_busqueda_vehiculo', {'form': form})


def eliminar_auto(request, id):
    try:
        auto = Vehiculo.objects.get(id=id)
    except Vehiculo.DoesNotExist:
        # Si el auto no se encuentra, renderizamos el template para auto no encontrado
        return render(request, 'inicio/resultado_auto_no_encontrado.html')
    
    # Si el auto existe, lo eliminamos
    auto.delete()
    
    # Después de eliminar el auto, redirigimos al catálogo de vehículos
    return redirect('catalogo_vehiculos')
