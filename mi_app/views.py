from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from mi_app.logica import controlador_usuario
import os
from django.contrib import messages


class Main:
    def open_index(self):
        return render(self, 'index.html')

    def open_registro(self):
        return render(self, 'registro.html')

    def open_administrar(self):
        return render(self, 'administrador.html')


class Logica:

    def controlador_administrador(request):
        if request.method == 'POST':uenos
        return render(request, 'administrador.html')

    def iniciar_sesion(request):
        retorno = None
        if request.method == 'POST':
            datos_usuario = dict()
            datos_usuario['correo'] = request.POST['correo']
            datos_usuario['usuario'] = request.POST['usuario']
            datos_usuario['password'] = request.POST['password']
            retorno = controlador_usuario.iniciar_sesion(datos_usuario)
        print('RETORNO: ', retorno)
        return render(request, 'index.html')

    def crear_usuario(request):
        retorno = None
        if request.method == 'POST':
            datos_usuario = dict()
            datos_usuario['username'] = request.POST['username']
            datos_usuario['email'] = request.POST['email']
            datos_usuario['email_recuperacion'] = request.POST['email_recuperacion']
            datos_usuario['password'] = request.POST['password']
            datos_usuario['numero'] = request.POST['numero']
            datos_usuario['ubicacion'] = request.POST['ubicacion']
            datos_usuario['estado'] = request.POST['estado']
            datos_usuario['ciudad'] = request.POST['ciudad']
            datos_usuario['nombre'] = request.POST['nombre']
            datos_usuario['apellido'] = request.POST['apellido']
            datos_usuario['fecha_nacimiento'] = request.POST['fecha_nacimiento']

            retorno = controlador_usuario.crear_usuario(datos_usuario)

        if retorno is not None and retorno is True:
            messages.info(request, 'Se ha creado el usuario correctamente!')
        else:
            messages.info(request, 'Error al crear el usuario!')

        return render(request, 'index.html', {'valor': 1, 'clase': ''})

    def predecir_imagen(request):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        if request.method == 'POST':
            imagen = request.FILES['elm_imagen']
            obj_file_sys_storage = FileSystemStorage()
            obj_file_sys_storage.save(imagen.name, imagen)
            url_imagen = base_dir + '/media/' + imagen.name
            porcentaje, clase = logica.predecir_imagen(url_imagen)

            # obj_image = Image(None, url_imagen, clase, porcentaje)
            # obj_image.save()

        return render(request, 'resultado.html', {'valor': porcentaje, 'clase': clase})
