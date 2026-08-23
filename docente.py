from usuario import Usuario


class Docente(Usuario):
    def __init__(self, cedula, nombre_completo, correo_electronico,
                 telefono, departamento, titulo_profesional):
        super().__init__(cedula, nombre_completo, correo_electronico, telefono)
        self.__departamento = departamento
        self.__titulo_profesional = titulo_profesional

    def get_departamento(self):
        return self.__departamento

    def get_titulo_profesional(self):
        return self.__titulo_profesional

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def set_titulo_profesional(self, titulo_profesional):
        self.__titulo_profesional = titulo_profesional

    def consultar_departamento(self):
        return f"Departamento: {self.__departamento}"

    def consultar_titulo_profesional(self):
        return f"Título: {self.__titulo_profesional}"
