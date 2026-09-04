from biblioteca import Biblioteca
from libro_fisico import LibroFisico
from libro_digital import LibroDigital
from estudiante import Estudiante
from docente import Docente
from cliente_mayorista import ClienteMayorista
from cliente_minorista import ClienteMinorista


def main():
    print("==============================================")
    print("       SISTEMA DE BIBLIOTECA")
    print("       SEMANAS 1 - 3 | ")
    print("==============================================")

    biblioteca = Biblioteca(
        "Biblioteca Central",
        "Av. Principal y Calle 10"
    )

    print("\nBiblioteca creada:")
    print(biblioteca.get_nombre())
    print(biblioteca.get_direccion())

    libro_fisico = LibroFisico(
        "L001",
        "Cien años de soledad",
        "Gabriel García Márquez",
        "Sudamericana",
        1967,
        "Estante A-10",
        471
    )

    libro_digital = LibroDigital(
        "L002",
        "El principito",
        "Antoine de Saint-Exupéry",
        "Salamandra",
        1943,
        "PDF",
        2.5,
        "https://biblioteca.com/libro/L002"
    )

    biblioteca.agregar_libro(libro_fisico)
    biblioteca.agregar_libro(libro_digital)

    estudiante = Estudiante(
        "0912345678",
        "Juan Pérez",
        "juan@gmail.com",
        "0999999999",
        "Ingeniería de Software",
        "Segundo"
    )

    docente = Docente(
        "0923456789",
        "María González",
        "maria@gmail.com",
        "0988888888",
        "Tecnología",
        "Ingeniera en Sistemas"
    )

    biblioteca.registrar_usuario(estudiante)
    biblioteca.registrar_usuario(docente)

    biblioteca.listar_libros()
    biblioteca.listar_usuarios()

    print("\n===== HERENCIA =====")
    print(estudiante.consultar_carrera())
    print(docente.consultar_departamento())
    print(docente.consultar_titulo_profesional())
    print(libro_fisico.consultar_ubicacion())
    print(libro_digital.descargar())

    print("\n===== ABSTRACCIÓN Y POLIMORFISMO =====")
    cliente_mayorista = ClienteMayorista("0991111111", "Carlos Torres", "carlos@gmail.com")
    cliente_minorista = ClienteMinorista("0992222222", "Ana López", "ana@gmail.com")
    monto = 100
    print("Descuento cliente mayorista:", cliente_mayorista.calcular_descuento(monto))
    print("Descuento cliente minorista:", cliente_minorista.calcular_descuento(monto))

    print("\n===== REALIZANDO PRÉSTAMO =====")
    prestamo = biblioteca.realizar_prestamo("0912345678", "L001")

    if prestamo is not None:
        print()
        prestamo.mostrar_informacion()

    print("\n===== ESTADO DEL LIBRO =====")
    libro = biblioteca.buscar_libro("L001")
    print("Libro:", libro.get_titulo())
    print("Estado:", libro.get_estado().value)

    biblioteca.listar_prestamos()

    print("\n===== DEVOLUCIÓN DEL LIBRO =====")
    if prestamo is not None:
        prestamo.cerrar_prestamo()
        print("Libro devuelto correctamente.")
        print("Estado:", libro.get_estado().value)

    print("\n===== ESTADO FINAL =====")
    biblioteca.listar_libros()

    print("\n==============================================")
    print("        PROGRAMA FINALIZADO")
    print("==============================================")


if __name__ == "__main__":
    main()
