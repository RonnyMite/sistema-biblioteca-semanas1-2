from libro import Libro


class LibroDigital(Libro):
    def __init__(self, codigo, titulo, autor, editorial, anio_publicacion,
                 formato, tamano_archivo, url_descarga):
        super().__init__(codigo, titulo, autor, editorial, anio_publicacion)
        self.__formato = formato
        self.__tamano_archivo = tamano_archivo
        self.__url_descarga = url_descarga

    def get_formato(self):
        return self.__formato

    def get_tamano_archivo(self):
        return self.__tamano_archivo

    def get_url_descarga(self):
        return self.__url_descarga

    def set_formato(self, formato):
        self.__formato = formato

    def set_tamano_archivo(self, tamano_archivo):
        self.__tamano_archivo = tamano_archivo

    def set_url_descarga(self, url_descarga):
        self.__url_descarga = url_descarga

    def descargar(self):
        return f"Descargando libro desde: {self.__url_descarga}"
