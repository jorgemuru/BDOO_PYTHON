# main.py

from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

# Crear instancia de UsuarioDAO
dao = UsuarioDAO()

# Crear un nuevo usuario
usuario01 = Usuario("1", "Juan Perez", "eljuan@ucu.edu.uy")
dao.crear_usuario(usuario01)

usuario02 = Usuario("2", "Juana Perez", "lajuana@ucu.edu.uy")
dao.crear_usuario(usuario02)

# Leer el usuario por ID
usuario_obtenido = dao.obtener_usuario("1")
if usuario_obtenido:
    print("1.- Nombre: ", usuario_obtenido.nombre, " || Email: ", usuario_obtenido.correo)

# Actualizar el usuario
usuario_obtenido.correo = "juan.perez@ucu.edu.uy"
dao.actualizar_usuario(usuario_obtenido)

# Listar todos los usuarios
usuarios = dao.listar_usuarios()
print("Lista de usuarios:")
for usuario in usuarios:
    print(".-", usuario.nombre, " || ", usuario.correo)

# Eliminar el usuario
#dao.eliminar_usuario("1")

#print("Lista de usuarios actualizada:")
#for usuario in usuarios:
#    print(".-", usuario.nombre, " || ", usuario.correo)


# Cerrar la conexión
dao.cerrar()
