from mi_app.models import Usuario


def iniciar_sesion(datos_usuario):
    usuarios = Usuario.objects.all()
    flag = False
    for item in usuarios.all(): # correo usuario password
        if item.email == datos_usuario['correo'] and item.username == datos_usuario['usuario'] and item.password == datos_usuario['password']:
            flag = True
    return flag


def crear_usuario(datos_usuario):
    print(datos_usuario)
    usuario = Usuario(id=None, username=datos_usuario['username'],
                      email=datos_usuario['email'],
                      email_recuperacion=datos_usuario['email_recuperacion'],
                      password=datos_usuario['password'],
                      numero=datos_usuario['numero'],
                      ubicacion=datos_usuario['ubicacion'],
                      estado=datos_usuario['estado'],
                      ciudad=datos_usuario['ciudad'],
                      nombre=datos_usuario['nombre'],
                      apellido=datos_usuario['apellido'],
                      fecha_nacimiento=datos_usuario['fecha_nacimiento'])
    try:
        usuario.save()
        return True
    except:
        return False
