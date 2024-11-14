from persistent import Persistent

class Usuario(Persistent):
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Usuario(id={self.id}, nombre={self.nombre}, correo={self.correo})"
