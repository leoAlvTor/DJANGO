from django.db import models


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(default='TEST')
    estado = models.TextField(default='DEFAULT')
    descripcion = models.TextField(default='DEFAULT VALUE')


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    email = models.TextField()
    email_recuperacion = models.TextField()
    password = models.TextField()
    numero = models.TextField()
    ubicacion = models.TextField()
    estado = models.TextField()
    ciudad = models.TextField()
    nombre = models.TextField()
    apellido = models.TextField()
    fecha_nacimiento = models.TextField()


# Entidad intermedia para una relacion muchos a muchos.
class Grupo_Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    # Foreign keys
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default=0)


class Red_Social(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(default='NA')
    url = models.TextField(default='NA')
    estado = models.TextField(default='NA')


class Parametro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(default='NA')
    token_parteA = models.TextField(default='NA')
    token_parteB = models.TextField(default='NA')
    # Foreign Keys
    red_social = models.ForeignKey(Red_Social, on_delete=models.CASCADE, default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)


class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='TESTING MESSAGE')
    hashtag = models.TextField(default='#TEST')
    link = models.TextField(default='https://www.google.com')
    ubicacion = models.TextField(default='NA')
    hora_envio = models.DateTimeField(null=True)
    estado = models.CharField(max_length=1, default='E')
    # Foreign Keys
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)
    grupo = models.ForeignKey(Grupo_Usuario, on_delete=models.CASCADE, default=0)
    red_social = models.ForeignKey(Red_Social, on_delete=models.CASCADE, default=0)
