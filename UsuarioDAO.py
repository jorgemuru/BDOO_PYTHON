import transaction
from ZODB import DB
from ZODB.FileStorage import FileStorage
import ZODB, ZODB.FileStorage

class UsuarioDAO:
    def __init__(self, db_path='usuarios.fs'):
        self.storage = FileStorage(db_path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        # Crear una colección de usuarios si no existe
        if 'usuarios' not in self.root:
            self.root['usuarios'] = {}

    # Create (Agregar un Usuario)
    def crear_usuario(self, usuario):
        self.root['usuarios'][usuario.id] = usuario
        transaction.commit()

    # Read (Obtener un Usuario por ID)
    def obtener_usuario(self, id):
        return self.root['usuarios'].get(id, None)

    # Update (Actualizar un Usuario)
    def actualizar_usuario(self, usuario):
        if usuario.id in self.root['usuarios']:
            self.root['usuarios'][usuario.id] = usuario
            transaction.commit()
        else:
            print("Usuario no encontrado")

    # Delete (Eliminar un Usuario)
    def eliminar_usuario(self, id):
        if id in self.root['usuarios']:
            del self.root['usuarios'][id]
            transaction.commit()
        else:
            print("Usuario no encontrado")

    # Listar todos los usuarios
    def listar_usuarios(self):
        return list(self.root['usuarios'].values())

    # Cerrar la conexión a la base de datos
    def cerrar(self):
        self.connection.close()
        self.db.close()
