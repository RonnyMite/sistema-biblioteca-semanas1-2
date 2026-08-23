from enum import Enum


class EstadoLibro(Enum):
    DISPONIBLE = "DISPONIBLE"
    PRESTADO = "PRESTADO"


class Libro:
    def __init__(self, codigo, titulo, autor, editorial, anio_publicacion):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__anio_publicacion = anio_publicacion
        self.__estado = EstadoLibro.DISPONIBLE

    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_editorial(self):
        return self.__editorial

    def get_anio_publicacion(self):
        return self.__anio_publicacion

    def get_estado(self):
        return self.__estado

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_editorial(self, editorial):
        self.__editorial = editorial

    def set_anio_publicacion(self, anio_publicacion):
        self.__anio_publicacion = anio_publicacion

    def set_estado(self, estado):
        self.__estado = estado

    def marcar_disponible(self):
        self.__estado = EstadoLibro.DISPONIBLE

    def marcar_prestado(self):
        self.__estado = EstadoLibro.PRESTADO

    def obtener_informacion(self):
        return (
            f"Código: {self.__codigo}\n"
            f"Título: {self.__titulo}\n"
            f"Autor: {self.__autor}\n"
            f"Editorial: {self.__editorial}\n"
            f"Año de publicación: {self.__anio_publicacion}\n"
            f"Estado: {self.__estado.value}"
        )
