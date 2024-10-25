from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    grupo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_producto_sku = models.ForeignKey('ProductoSKU', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventario'

    def __str__(self):
        return f'Inventario {self.id_inventario}'


class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    class Meta:
        db_table = 'perfil'

    def __str__(self):
        return self.nombre


class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    numero_control = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)

    class Meta:
        db_table = 'personal'

    def __str__(self):
        return self.nombre


class ProductoLPN(models.Model):
    id_producto_lpn = models.AutoField(primary_key=True)
    id_producto_sku = models.ForeignKey('ProductoSKU', on_delete=models.SET_NULL, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', on_delete=models.SET_NULL, null=True)
    id_estado = models.ForeignKey('Estado', on_delete=models.SET_NULL, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    id_personal = models.ForeignKey('Personal', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'productolpn'

    def __str__(self):
        return f'Producto LPN {self.id_producto_lpn}'


class ProductoSKU(models.Model):
    id_producto_sku = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'productosku'

    def __str__(self):
        return self.nombre


class TipoTransaccion(models.Model):
    id_tipo_transaccion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipo_transaccion'

    def __str__(self):
        return self.descripcion


class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    id_producto_lpn = models.ForeignKey(ProductoLPN, on_delete=models.SET_NULL, null=True)
    tipo_transaccion = models.CharField(max_length=50, choices=[
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
        ('Actualización', 'Actualización')
    ])
    descripcion = models.TextField(null=True, blank=True)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    id_tipo_transaccion = models.ForeignKey(TipoTransaccion, on_delete=models.SET_NULL, null=True)
    historial = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'transaccion'

    def __str__(self):
        return f'Transacción {self.id_transaccion}'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    eje1 = models.CharField(max_length=100, null=True, blank=True)
    eje2 = models.CharField(max_length=100, null=True, blank=True)
    eje3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'ubicacion'

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, choices=[
        ('Administrador', 'Administrador'),
        ('Responsable', 'Responsable'),
        ('Usuario', 'Usuario')
    ])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo')
    ], default='Activo')
    id_perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre
