from django import forms 
from django.contrib.auth.models import User # modelo gestion de usuarios 
from django.contrib.auth.forms import UserCreationForm # modelo creacion de usuarios
from .models import Producto

class RegistroForm(UserCreationForm):
    class Meta: # Meta se utiliza para definir informacion adicional del formulario
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cog', 'descripcion', 'grupo', 'cantidad']
