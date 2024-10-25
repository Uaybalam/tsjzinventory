from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import (
    Categoria, ProductoSKU, Estado, Ubicacion,
    Personal, ProductoLPN, Inventario, TipoTransaccion,
    Transaccion, Perfil, Usuario
)

class RegistroForm(UserCreationForm):
    class Meta: # Meta se utiliza para definir informacion adicional del formulario
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'grupo']


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['id_producto_sku', 'cantidad']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'rol']


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['numero_control', 'nombre', 'puesto']


class ProductoLPNForm(forms.ModelForm):
    class Meta:
        model = ProductoLPN
        fields = ['id_producto_sku', 'id_ubicacion', 'id_estado', 'id_personal']


class ProductoSKUForm(forms.ModelForm):
    class Meta:
        model = ProductoSKU
        fields = ['nombre', 'descripcion', 'id_categoria']


class TipoTransaccionForm(forms.ModelForm):
    class Meta:
        model = TipoTransaccion
        fields = ['descripcion']


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['id_producto_lpn', 'tipo_transaccion', 'descripcion', 'id_tipo_transaccion', 'historial']


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'descripcion', 'eje1', 'eje2', 'eje3']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contrasena', 'rol', 'estado', 'id_perfil']
        widgets = {
            'contrasena': forms.PasswordInput(),  # Para ocultar la contraseña al ingresar
        }