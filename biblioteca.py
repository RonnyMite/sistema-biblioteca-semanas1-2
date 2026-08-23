class Biblioteca:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion

        # Composición: la biblioteca contiene estas colecciones.
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def agregar_libro(self, libro):
        self.__libros.append(libro)
        print("Libro agregado correctamente.")

    def eliminar_libro(self, codigo):
        for libro in self.__libros:
            if libro.get_codigo() == codigo:
                self.__libros.remove(libro)
                print("Libro eliminado correctamente.")
                return
        print("Libro no encontrado.")

    def buscar_libro(self, codigo):
        for libro in self.__libros:
            if libro.get_codigo() == codigo:
                return libro
        return None

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, cedula):
        for usuario in self.__usuarios:
            if usuario.get_cedula() == cedula:
                self.__usuarios.remove(usuario)
                print("Usuario eliminado correctamente.")
                return
        print("Usuario no encontrado.")

    def buscar_usuario(self, cedula):
        for usuario in self.__usuarios:
            if usuario.get_cedula() == cedula:
                return usuario
        return None

    def realizar_prestamo(self, cedula, codigo):
        usuario = self.buscar_usuario(cedula)
        libro = self.buscar_libro(codigo)

        if usuario is None:
            print("Usuario no encontrado.")
            return None

        if libro is None:
            print("Libro no encontrado.")
            return None

        prestamo = usuario.realizar_prestamo(libro)

        if prestamo is not None:
            self.__prestamos.append(prestamo)
            print("Préstamo realizado correctamente.")

        return prestamo

    def listar_libros(self):
        print("\n===== LIBROS DE LA BIBLIOTECA =====")
        for libro in self.__libros:
            print(
                f"{libro.get_codigo()} - "
                f"{libro.get_titulo()} - "
                f"{libro.get_estado().value}"
            )

    def listar_usuarios(self):
        print("\n===== USUARIOS DE LA BIBLIOTECA =====")
        for usuario in self.__usuarios:
            print(
                f"{usuario.get_cedula()} - "
                f"{usuario.get_nombre_completo()}"
            )

    def listar_prestamos(self):
        print("\n===== PRÉSTAMOS =====")
        for prestamo in self.__prestamos:
            prestamo.mostrar_informacion()
            print()
