from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.contrib import messages
from .models import (
    Categoria, ProductoSKU, Estado, Ubicacion,
    Personal, ProductoLPN, Inventario, TipoTransaccion,
    Transaccion, Perfil, Usuario
)
from .forms import (
    CategoriaForm, ProductoSKUForm, EstadoForm, UbicacionForm,
    PersonalForm, ProductoLPNForm, InventarioForm,
    TipoTransaccionForm, TransaccionForm, PerfilForm, UsuarioForm
)


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registration/registro.html', {'form': form, 'error': 'Error en el formulario'})
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
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
            print("Formulario inválido")
            return render(request, 'login.html', {'form': form, 'error': 'Formulario inválido'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión con éxito.')
    return redirect('login')  # Redirigir al login después de cerrar sesión

@login_required
def dashboard(request):
    query = request.GET.get('query')  # Capturamos el término de búsqueda del formulario
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)  # Filtrar productos por nombre que contiene el término
    else:
        productos = Producto.objects.all()  # Si no hay término de búsqueda, muestra todos los productos
    total_productos = productos.count()
    return render(request, 'dashboard.html', {
        'productos': productos,
        'total_productos': total_productos,
    })
@login_required
# Vistas para Categoria
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})
@login_required
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})
@login_required
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria_form.html', {'form': form})
@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categoria_confirm_delete.html', {'categoria': categoria})
@login_required
# Vistas para ProductoSKU
def producto_sku_list(request):
    productos = ProductoSKU.objects.all()
    return render(request, 'producto_sku_list.html', {'productos': productos})
@login_required
def producto_sku_create(request):
    if request.method == 'POST':
        form = ProductoSKUForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_sku_list')
    else:
        form = ProductoSKUForm()
    return render(request, 'producto_sku_form.html', {'form': form})
@login_required
def producto_sku_update(request, pk):
    producto = get_object_or_404(ProductoSKU, pk=pk)
    if request.method == 'POST':
        form = ProductoSKUForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_sku_list')
    else:
        form = ProductoSKUForm(instance=producto)
    return render(request, 'producto_sku_form.html', {'form': form})
@login_required
def producto_sku_delete(request, pk):
    producto = get_object_or_404(ProductoSKU, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_sku_list')
    return render(request, 'producto_sku_confirm_delete.html', {'producto': producto})
@login_required
# Vistas para Estado
def estado_list(request):
    estados = Estado.objects.all()
    return render(request, 'estado_list.html', {'estados': estados})
@login_required
def estado_create(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_list')
    else:
        form = EstadoForm()
    return render(request, 'estado_form.html', {'form': form})
@login_required
def estado_update(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return redirect('estado_list')
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'estado_form.html', {'form': form})
@login_required
def estado_delete(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == 'POST':
        estado.delete()
        return redirect('estado_list')
    return render(request, 'estado_confirm_delete.html', {'estado': estado})
@login_required
# Vistas para Ubicacion
def ubicacion_list(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'ubicacion_list.html', {'ubicaciones': ubicaciones})
@login_required
def ubicacion_create(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ubicacion_list')
    else:
        form = UbicacionForm()
    return render(request, 'ubicacion_form.html', {'form': form})
@login_required
def ubicacion_update(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('ubicacion_list')
    else:
        form = UbicacionForm(instance=ubicacion)
    return render(request, 'ubicacion_form.html', {'form': form})
@login_required
def ubicacion_delete(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('ubicacion_list')
    return render(request, 'ubicacion_confirm_delete.html', {'ubicacion': ubicacion})
@login_required
# Vistas para Personal
def personal_list(request):
    personales = Personal.objects.all()
    return render(request, 'personal_list.html', {'personales': personales})
@login_required
def personal_create(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm()
    return render(request, 'personal_form.html', {'form': form})
@login_required
def personal_update(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'personal_form.html', {'form': form})
@login_required
def personal_delete(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        personal.delete()
        return redirect('personal_list')
    return render(request, 'personal_confirm_delete.html', {'personal': personal})
@login_required
# Vistas para ProductoLPN
def producto_lpn_list(request):
    productos_lpn = ProductoLPN.objects.all()
    return render(request, 'producto_lpn_list.html', {'productos_lpn': productos_lpn})
@login_required
def producto_lpn_create(request):
    if request.method == 'POST':
        form = ProductoLPNForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lpn_list')
    else:
        form = ProductoLPNForm()
    return render(request, 'producto_lpn_form.html', {'form': form})
@login_required
def producto_lpn_update(request, pk):
    producto_lpn = get_object_or_404(ProductoLPN, pk=pk)
    if request.method == 'POST':
        form = ProductoLPNForm(request.POST, instance=producto_lpn)
        if form.is_valid():
            form.save()
            return redirect('producto_lpn_list')
    else:
        form = ProductoLPNForm(instance=producto_lpn)
    return render(request, 'producto_lpn_form.html', {'form': form})
@login_required
def producto_lpn_delete(request, pk):
    producto_lpn = get_object_or_404(ProductoLPN, pk=pk)
    if request.method == 'POST':
        producto_lpn.delete()
        return redirect('producto_lpn_list')
    return render(request, 'producto_lpn_confirm_delete.html', {'producto_lpn': producto_lpn})
@login_required
# Vistas para Inventario
def inventario_list(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario_list.html', {'inventarios': inventarios})
@login_required
def inventario_create(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario_list')
    else:
        form = InventarioForm()
    return render(request, 'inventario_form.html', {'form': form})
@login_required
def inventario_update(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('inventario_list')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inventario_form.html', {'form': form})
@login_required
def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inventario_list')
    return render(request, 'inventario_confirm_delete.html', {'inventario': inventario})
@login_required
# Vistas para TipoTransaccion
def tipo_transaccion_list(request):
    tipos_transaccion = TipoTransaccion.objects.all()
    return render(request, 'tipo_transaccion_list.html', {'tipos_transaccion': tipos_transaccion})
@login_required
def tipo_transaccion_create(request):
    if request.method == 'POST':
        form = TipoTransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_transaccion_list')
    else:
        form = TipoTransaccionForm()
    return render(request, 'tipo_transaccion_form.html', {'form': form})

@login_required
def tipo_transaccion_update(request, pk):
    tipo_transaccion = get_object_or_404(TipoTransaccion, pk=pk)
    if request.method == 'POST':
        form = TipoTransaccionForm(request.POST, instance=tipo_transaccion)
        if form.is_valid():
            form.save()
            return redirect('tipo_transaccion_list')
    else:
        form = TipoTransaccionForm(instance=tipo_transaccion)
    return render(request, 'tipo_transaccion_form.html', {'form': form})
@login_required
def tipo_transaccion_delete(request, pk):
    tipo_transaccion = get_object_or_404(TipoTransaccion, pk=pk)
    if request.method == 'POST':
        tipo_transaccion.delete()
        return redirect('tipo_transaccion_list')
    return render(request, 'tipo_transaccion_confirm_delete.html', {'tipo_transaccion': tipo_transaccion})
@login_required
# Vistas para Transaccion
def transaccion_list(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'transaccion_list.html', {'transacciones': transacciones})
@login_required
def transaccion_create(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaccion_list')
    else:
        form = TransaccionForm()
    return render(request, 'transaccion_form.html', {'form': form})
@login_required
def transaccion_update(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            return redirect('transaccion_list')
    else:
        form = TransaccionForm(instance=transaccion)
    return render(request, 'transaccion_form.html', {'form': form})
@login_required
def transaccion_delete(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        transaccion.delete()
        return redirect('transaccion_list')
    return render(request, 'transaccion_confirm_delete.html', {'transaccion': transaccion})
@login_required
# Vistas para Perfil
def perfil_list(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfil_list.html', {'perfiles': perfiles})
@login_required
def perfil_create(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_list')
    else:
        form = PerfilForm()
    return render(request, 'perfil_form.html', {'form': form})
@login_required
def perfil_update(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_list')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil_form.html', {'form': form})
@login_required
def perfil_delete(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfil_list')
    return render(request, 'perfil_confirm_delete.html', {'perfil': perfil})
@login_required
# Vistas para Usuario
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})
@login_required
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'usuario_form.html', {'form': form})
@login_required
def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_form.html', {'form': form})
@login_required
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})