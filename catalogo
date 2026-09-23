class Catalogo:

    def __init__(self):
        # LIST: almacena todos los libros
        self.__libros = []

        # DICT: permite buscar rápidamente por código
        self.__libros_por_codigo = {}

        # SET: evita códigos duplicados
        self.__codigos = set()

    def agregar_libro(self, libro):
        codigo = libro.get_codigo()

        if codigo in self.__codigos:
            return False

        self.__libros.append(libro)
        self.__libros_por_codigo[codigo] = libro
        self.__codigos.add(codigo)

        return True

    def buscar_libro(self, codigo):
        return self.__libros_por_codigo.get(codigo)

    def listar_libros(self):
        return self.__libros.copy()

    def actualizar_libro(
        self,
        codigo,
        titulo,
        autor,
        editorial,
        anio_publicacion
    ):
        libro = self.buscar_libro(codigo)

        if libro is None:
            return False

        libro.set_titulo(titulo)
        libro.set_autor(autor)
        libro.set_editorial(editorial)
        libro.set_anio_publicacion(anio_publicacion)

        return True

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)

        if libro is None:
            return False

        self.__libros.remove(libro)
        del self.__libros_por_codigo[codigo]
        self.__codigos.remove(codigo)

        return True

    def existe_codigo(self, codigo):
        return codigo in self.__codigos

    def cantidad_libros(self):
        return len(self.__libros)

    def mostrar_catalogo(self):
        print("\n===== CATÁLOGO DE LIBROS =====")

        if not self.__libros:
            print("El catálogo está vacío.")
            return

        for libro in self.__libros:
            print(
                f"{libro.get_codigo()} - "
                f"{libro.get_titulo()} - "
                f"{libro.get_autor()} - "
                f"{libro.get_estado().value}"
            )
