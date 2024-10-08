from django.shortcuts import render, redirect #render: Para generar una respuesta HTML basada en plantillas y enviarla al usuario. redirect: Para redirigir a una URL diferente (por ejemplo, después del login o registro exitoso).
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Producto
from .forms import ProductoForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(f"Usuario autenticado: {user}")
                login(request, user)
                return redirect('dashboard')
            else:
                print("Error de autenticación")
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas'})
        else:
            # Añadir un mensaje de error si el formulario no es válido
            return render(request, 'login.html', {'form': form, 'error': 'Formulario inválido'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login.html')  # Redirigir al login después de cerrar sesión

@login_required
def dashboard(request):
    print(request.user)
    productos = Producto.objects.all()  # Obtén todos los productos
    total_productos = productos.count()
    return render(request, 'dashboard.html',{
        'productos': productos,
        'total_productos' : total_productos
    })    

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST' :
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form':form})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('dashboard')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

        
    