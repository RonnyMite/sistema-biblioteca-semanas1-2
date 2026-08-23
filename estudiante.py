from usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, cedula, nombre_completo, correo_electronico,
                 telefono, carrera, nivel):
        super().__init__(cedula, nombre_completo, correo_electronico, telefono)
        self.__carrera = carrera
        self.__nivel = nivel

    def get_carrera(self):
        return self.__carrera

    def get_nivel(self):
        return self.__nivel

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def consultar_carrera(self):
        return f"Carrera: {self.__carrera} | Nivel: {self.__nivel}"
