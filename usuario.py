class Usuario:
    def __init__(self, cedula, nombre_completo, correo_electronico, telefono):
        self.__cedula = cedula
        self.__nombre_completo = nombre_completo
        self.__correo_electronico = correo_electronico
        self.__telefono = telefono
        self.__prestamos = []

    def get_cedula(self):
        return self.__cedula

    def get_nombre_completo(self):
        return self.__nombre_completo

    def get_correo_electronico(self):
        return self.__correo_electronico

    def get_telefono(self):
        return self.__telefono

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_nombre_completo(self, nombre_completo):
        self.__nombre_completo = nombre_completo

    def set_correo_electronico(self, correo_electronico):
        self.__correo_electronico = correo_electronico

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def realizar_prestamo(self, libro):
        from prestamo import Prestamo

        if libro.get_estado().value == "DISPONIBLE":
            prestamo = Prestamo(libro, self)
            self.__prestamos.append(prestamo)
            libro.marcar_prestado()
            return prestamo

        print("El libro no está disponible.")
        return None

    def ver_historial_prestamos(self):
        return self.__prestamos
