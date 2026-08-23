from datetime import date


class Prestamo:
    def __init__(self, libro, usuario):
        self.__fecha_inicio = date.today()
        self.__fecha_devolucion = None
        self.__libro = libro
        self.__usuario = usuario

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def get_libro(self):
        return self.__libro

    def get_usuario(self):
        return self.__usuario

    def set_fecha_inicio(self, fecha):
        self.__fecha_inicio = fecha

    def set_fecha_devolucion(self, fecha):
        self.__fecha_devolucion = fecha

    def set_libro(self, libro):
        self.__libro = libro

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def calcular_dias_prestamo(self):
        if self.__fecha_devolucion is None:
            return (date.today() - self.__fecha_inicio).days
        return (self.__fecha_devolucion - self.__fecha_inicio).days

    def esta_vencido(self):
        return self.__fecha_devolucion is None

    def cerrar_prestamo(self):
        self.__fecha_devolucion = date.today()
        self.__libro.marcar_disponible()

    def mostrar_informacion(self):
        print("----- INFORMACIÓN DEL PRÉSTAMO -----")
        print("Libro:", self.__libro.get_titulo())
        print("Usuario:", self.__usuario.get_nombre_completo())
        print("Fecha de inicio:", self.__fecha_inicio)
        print("Fecha de devolución:", self.__fecha_devolucion)
