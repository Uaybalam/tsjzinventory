from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view
from .views import (
    categoria_list, categoria_create, categoria_update, categoria_delete,
    producto_sku_list, producto_sku_create, producto_sku_update, producto_sku_delete,
    estado_list, estado_create, estado_update, estado_delete,
    ubicacion_list, ubicacion_create, ubicacion_update, ubicacion_delete,
    personal_list, personal_create, personal_update, personal_delete,
    producto_lpn_list, producto_lpn_create, producto_lpn_update, producto_lpn_delete,
    inventario_list, inventario_create, inventario_update, inventario_delete,
    tipo_transaccion_list, tipo_transaccion_create, tipo_transaccion_update, tipo_transaccion_delete,
    transaccion_list, transaccion_create, transaccion_update, transaccion_delete,
    perfil_list, perfil_create, perfil_update, perfil_delete,
    usuario_list, usuario_create, usuario_update, usuario_delete,
)

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
     # Rutas para Categoria
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/nueva/', categoria_create, name='categoria_create'),
    path('categorias/editar/<int:pk>/', categoria_update, name='categoria_update'),
    path('categorias/eliminar/<int:pk>/', categoria_delete, name='categoria_delete'),

    # Rutas para ProductoSKU
    path('productos_sku/', producto_sku_list, name='producto_sku_list'),
    path('productos_sku/nuevo/', producto_sku_create, name='producto_sku_create'),
    path('productos_sku/editar/<int:pk>/', producto_sku_update, name='producto_sku_update'),
    path('productos_sku/eliminar/<int:pk>/', producto_sku_delete, name='producto_sku_delete'),

    # Rutas para Estado
    path('estados/', estado_list, name='estado_list'),
    path('estados/nuevo/', estado_create, name='estado_create'),
    path('estados/editar/<int:pk>/', estado_update, name='estado_update'),
    path('estados/eliminar/<int:pk>/', estado_delete, name='estado_delete'),

    # Rutas para Ubicacion
    path('ubicaciones/', ubicacion_list, name='ubicacion_list'),
    path('ubicaciones/nueva/', ubicacion_create, name='ubicacion_create'),
    path('ubicaciones/editar/<int:pk>/', ubicacion_update, name='ubicacion_update'),
    path('ubicaciones/eliminar/<int:pk>/', ubicacion_delete, name='ubicacion_delete'),

    # Rutas para Personal
    path('personales/', personal_list, name='personal_list'),
    path('personales/nuevo/', personal_create, name='personal_create'),
    path('personales/editar/<int:pk>/', personal_update, name='personal_update'),
    path('personales/eliminar/<int:pk>/', personal_delete, name='personal_delete'),

    # Rutas para ProductoLPN
    path('productos_lpn/', producto_lpn_list, name='producto_lpn_list'),
    path('productos_lpn/nuevo/', producto_lpn_create, name='producto_lpn_create'),
    path('productos_lpn/editar/<int:pk>/', producto_lpn_update, name='producto_lpn_update'),
    path('productos_lpn/eliminar/<int:pk>/', producto_lpn_delete, name='producto_lpn_delete'),

    # Rutas para Inventario
    path('inventarios/', inventario_list, name='inventario_list'),
    path('inventarios/nuevo/', inventario_create, name='inventario_create'),
    path('inventarios/editar/<int:pk>/', inventario_update, name='inventario_update'),
    path('inventarios/eliminar/<int:pk>/', inventario_delete, name='inventario_delete'),

    # Rutas para TipoTransaccion
    path('tipos_transaccion/', tipo_transaccion_list, name='tipo_transaccion_list'),
    path('tipos_transaccion/nuevo/', tipo_transaccion_create, name='tipo_transaccion_create'),
    path('tipos_transaccion/editar/<int:pk>/', tipo_transaccion_update, name='tipo_transaccion_update'),
    path('tipos_transaccion/eliminar/<int:pk>/', tipo_transaccion_delete, name='tipo_transaccion_delete'),

    # Rutas para Transaccion
    path('transacciones/', transaccion_list, name='transaccion_list'),
    path('transacciones/nueva/', transaccion_create, name='transaccion_create'),
    path('transacciones/editar/<int:pk>/', transaccion_update, name='transaccion_update'),
    path('transacciones/eliminar/<int:pk>/', transaccion_delete, name='transaccion_delete'),

    # Rutas para Perfil
    path('perfiles/', perfil_list, name='perfil_list'),
    path('perfiles/nuevo/', perfil_create, name='perfil_create'),
    path('perfiles/editar/<int:pk>/', perfil_update, name='perfil_update'),
    path('perfiles/eliminar/<int:pk>/', perfil_delete, name='perfil_delete'),

    # Rutas para Usuario
    path('usuarios/', usuario_list, name='usuario_list'),
    path('usuarios/nuevo/', usuario_create, name='usuario_create'),
    path('usuarios/editar/<int:pk>/', usuario_update, name='usuario_update'),
    path('usuarios/eliminar/<int:pk>/', usuario_delete, name='usuario_delete'),
    
]