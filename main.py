from biblioteca import Biblioteca
from libro_fisico import LibroFisico
from libro_digital import LibroDigital
from estudiante import Estudiante
from docente import Docente
from cliente_mayorista import ClienteMayorista
from cliente_minorista import ClienteMinorista
from catalogo import Catalogo

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
# ==================================================
    # SEMANA 5 - COLECCIONES
    # ==================================================

    print("\n")
    print("==============================================")
    print("       SEMANA 5 - COLECCIONES")
    print("       CATÁLOGO DE LIBROS")
    print("==============================================")

    catalogo = Catalogo()

    # Agregar los libros que ya fueron creados
    print("\n===== AGREGANDO LIBROS AL CATÁLOGO =====")

    if catalogo.agregar_libro(libro_fisico):
        print("Libro L001 agregado correctamente.")

    if catalogo.agregar_libro(libro_digital):
        print("Libro L002 agregado correctamente.")

    # Crear otro libro utilizando una clase que ya existe
    libro_fisico2 = LibroFisico(
        "L003",
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
        "Editorial Planeta",
        1605,
        "Estante B-05",
        863
    )

    if catalogo.agregar_libro(libro_fisico2):
        print("Libro L003 agregado correctamente.")

    # ==========================================
    # EVITAR DUPLICADOS
    # ==========================================

    print("\n===== VALIDACIÓN DE DUPLICADOS =====")

    libro_duplicado = LibroFisico(
        "L001",
        "Otro libro",
        "Otro autor",
        "Otra editorial",
        2020,
        "Estante C-01",
        200
    )

    if catalogo.agregar_libro(libro_duplicado):
        print("Libro agregado.")
    else:
        print("No se puede agregar: el código L001 ya existe.")

    # ==========================================
    # LISTAR
    # ==========================================

    print("\n===== LISTAR CATÁLOGO =====")
    catalogo.mostrar_catalogo()

    # ==========================================
    # BUSCAR
    # ==========================================

    print("\n===== BUSCAR LIBRO =====")

    libro_buscado = catalogo.buscar_libro("L002")

    if libro_buscado:
        print("Libro encontrado:")
        print(libro_buscado.obtener_informacion())
    else:
        print("Libro no encontrado.")

    # ==========================================
    # ACTUALIZAR
    # ==========================================

    print("\n===== ACTUALIZAR LIBRO =====")

    actualizado = catalogo.actualizar_libro(
        "L002",
        "El Principito - Edición Especial",
        "Antoine de Saint-Exupéry",
        "Salamandra",
        1943
    )

    if actualizado:
        print("Libro actualizado correctamente.")
    else:
        print("Libro no encontrado.")

    catalogo.mostrar_catalogo()

    # ==========================================
    # ELIMINAR
    # ==========================================

    print("\n===== ELIMINAR LIBRO =====")

    eliminado = catalogo.eliminar_libro("L003")

    if eliminado:
        print("Libro eliminado correctamente.")
    else:
        print("Libro no encontrado.")

    catalogo.mostrar_catalogo()

    # ==========================================
    # CANTIDAD
    # ==========================================

    print("\nCantidad de libros en el catálogo:")
    print(catalogo.cantidad_libros())

    print("\n==============================================")
    print("       SEMANA 5 FINALIZADA")
    print("==============================================")

if __name__ == "__main__":
    main()
