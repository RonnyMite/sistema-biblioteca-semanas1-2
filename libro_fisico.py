from libro import Libro


class LibroFisico(Libro):
    def __init__(self, codigo, titulo, autor, editorial, anio_publicacion,
                 ubicacion, numero_paginas):
        super().__init__(codigo, titulo, autor, editorial, anio_publicacion)
        self.__ubicacion = ubicacion
        self.__numero_paginas = numero_paginas

    def get_ubicacion(self):
        return self.__ubicacion

    def get_numero_paginas(self):
        return self.__numero_paginas

    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def set_numero_paginas(self, numero_paginas):
        self.__numero_paginas = numero_paginas

    def consultar_ubicacion(self):
        return f"Ubicación del libro: {self.__ubicacion}"
