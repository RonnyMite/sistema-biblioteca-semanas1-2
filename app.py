import flet as ft

from catalogo import Catalogo
from libro_fisico import LibroFisico
from libro_digital import LibroDigital


def main(page: ft.Page):

    # ==========================================
    # CONFIGURACIÓN DE LA VENTANA
    # ==========================================

    page.title = "Sistema de Biblioteca"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    catalogo = Catalogo()

    # ==========================================
    # CAMPOS DEL FORMULARIO
    # ==========================================

    codigo = ft.TextField(
        label="Código",
        hint_text="Ejemplo: L001",
        width=220
    )

    titulo = ft.TextField(
        label="Título",
        hint_text="Título del libro",
        width=300
    )

    autor = ft.TextField(
        label="Autor",
        hint_text="Autor del libro",
        width=300
    )

    editorial = ft.TextField(
        label="Editorial",
        hint_text="Editorial",
        width=250
    )

    anio = ft.TextField(
        label="Año de publicación",
        hint_text="Ejemplo: 2020",
        width=220
    )

    tipo = ft.Dropdown(
        label="Tipo de libro",
        width=220,
        options=[
            ft.dropdown.Option("Físico"),
            ft.dropdown.Option("Digital")
        ]
    )

    ubicacion = ft.TextField(
        label="Ubicación",
        hint_text="Ejemplo: Estante A-01",
        width=250
    )

    paginas = ft.TextField(
        label="Número de páginas",
        hint_text="Ejemplo: 300",
        width=220
    )

    formato = ft.TextField(
        label="Formato digital",
        hint_text="Ejemplo: PDF",
        width=220
    )

    tamano = ft.TextField(
        label="Tamaño del archivo",
        hint_text="Ejemplo: 2.5 MB",
        width=220
    )

    url = ft.TextField(
        label="URL de descarga",
        hint_text="https://...",
        width=350
    )

    mensaje = ft.Text("", size=16)

    cantidad = ft.Text(
        "Total de libros: 0",
        size=18
    )

    # ==========================================
    # TABLA
    # ==========================================

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Autor")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Estado")),
        ],
        rows=[]
    )

    # ==========================================
    # FUNCIONES AUXILIARES
    # ==========================================

    def mostrar_mensaje(texto):
        mensaje.value = texto
        page.update()

    def limpiar_campos():

        codigo.value = ""
        titulo.value = ""
        autor.value = ""
        editorial.value = ""
        anio.value = ""
        tipo.value = None
        ubicacion.value = ""
        paginas.value = ""
        formato.value = ""
        tamano.value = ""
        url.value = ""

        page.update()

    def actualizar_tabla():

        tabla.rows.clear()

        for libro in catalogo.listar_libros():

            if isinstance(libro, LibroFisico):
                tipo_libro = "Físico"
            elif isinstance(libro, LibroDigital):
                tipo_libro = "Digital"
            else:
                tipo_libro = "Libro"

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(libro.get_codigo())
                        ),
                        ft.DataCell(
                            ft.Text(libro.get_titulo())
                        ),
                        ft.DataCell(
                            ft.Text(libro.get_autor())
                        ),
                        ft.DataCell(
                            ft.Text(tipo_libro)
                        ),
                        ft.DataCell(
                            ft.Text(
                                libro.get_estado().value
                            )
                        ),
                    ]
                )
            )

        cantidad.value = (
            f"Total de libros: "
            f"{catalogo.cantidad_libros()}"
        )

        page.update()

    # ==========================================
    # AGREGAR
    # ==========================================

    def agregar_click(e):

        codigo_valor = codigo.value.strip()
        titulo_valor = titulo.value.strip()
        autor_valor = autor.value.strip()
        editorial_valor = editorial.value.strip()
        anio_valor = anio.value.strip()
        tipo_valor = tipo.value

        if not codigo_valor:
            mostrar_mensaje(
                "Error: ingrese el código."
            )
            return

        if not titulo_valor:
            mostrar_mensaje(
                "Error: ingrese el título."
            )
            return

        if not autor_valor:
            mostrar_mensaje(
                "Error: ingrese el autor."
            )
            return

        if not editorial_valor:
            mostrar_mensaje(
                "Error: ingrese la editorial."
            )
            return

        if not anio_valor:
            mostrar_mensaje(
                "Error: ingrese el año."
            )
            return

        if tipo_valor is None:
            mostrar_mensaje(
                "Error: seleccione el tipo de libro."
            )
            return

        try:
            anio_valor = int(anio_valor)
        except ValueError:
            mostrar_mensaje(
                "Error: el año debe ser numérico."
            )
            return

        if catalogo.existe_codigo(codigo_valor):
            mostrar_mensaje(
                "Error: el código ya existe."
            )
            return

        # ======================================
        # LIBRO FÍSICO
        # ======================================

        if tipo_valor == "Físico":

            ubicacion_valor = ubicacion.value.strip()
            paginas_valor = paginas.value.strip()

            if not ubicacion_valor:
                mostrar_mensaje(
                    "Ingrese la ubicación."
                )
                return

            if not paginas_valor:
                mostrar_mensaje(
                    "Ingrese el número de páginas."
                )
                return

            try:
                paginas_valor = int(paginas_valor)
            except ValueError:
                mostrar_mensaje(
                    "Las páginas deben ser numéricas."
                )
                return

            libro = LibroFisico(
                codigo_valor,
                titulo_valor,
                autor_valor,
                editorial_valor,
                anio_valor,
                ubicacion_valor,
                paginas_valor
            )

        # ======================================
        # LIBRO DIGITAL
        # ======================================

        else:

            formato_valor = formato.value.strip()
            tamano_valor = tamano.value.strip()
            url_valor = url.value.strip()

            if not formato_valor:
                mostrar_mensaje(
                    "Ingrese el formato."
                )
                return

            if not tamano_valor:
                mostrar_mensaje(
                    "Ingrese el tamaño del archivo."
                )
                return

            if not url_valor:
                mostrar_mensaje(
                    "Ingrese la URL de descarga."
                )
                return

            try:
                tamano_valor = float(tamano_valor)
            except ValueError:
                mostrar_mensaje(
                    "El tamaño debe ser numérico."
                )
                return

            libro = LibroDigital(
                codigo_valor,
                titulo_valor,
                autor_valor,
                editorial_valor,
                anio_valor,
                formato_valor,
                tamano_valor,
                url_valor
            )

        if catalogo.agregar_libro(libro):

            mostrar_mensaje(
                "Libro agregado correctamente."
            )

            limpiar_campos()
            actualizar_tabla()

    # ==========================================
    # BUSCAR
    # ==========================================

    def buscar_click(e):

        codigo_valor = codigo.value.strip()

        if not codigo_valor:
            mostrar_mensaje(
                "Ingrese el código que desea buscar."
            )
            return

        libro = catalogo.buscar_libro(codigo_valor)

        if libro is None:
            mostrar_mensaje(
                "Libro no encontrado."
            )
            return

        titulo.value = libro.get_titulo()
        autor.value = libro.get_autor()
        editorial.value = libro.get_editorial()
        anio.value = str(
            libro.get_anio_publicacion()
        )

        if isinstance(libro, LibroFisico):

            tipo.value = "Físico"
            ubicacion.value = libro.get_ubicacion()
            paginas.value = str(
                libro.get_numero_paginas()
            )

        elif isinstance(libro, LibroDigital):

            tipo.value = "Digital"
            formato.value = libro.get_formato()
            tamano.value = str(
                libro.get_tamano_archivo()
            )
            url.value = libro.get_url_descarga()

        mostrar_mensaje(
            "Libro encontrado correctamente."
        )

        page.update()

    # ==========================================
    # ACTUALIZAR
    # ==========================================

    def actualizar_click(e):

        codigo_valor = codigo.value.strip()

        if not codigo_valor:
            mostrar_mensaje(
                "Ingrese el código del libro."
            )
            return

        libro = catalogo.buscar_libro(
            codigo_valor
        )

        if libro is None:
            mostrar_mensaje(
                "El libro no existe."
            )
            return

        titulo_valor = titulo.value.strip()
        autor_valor = autor.value.strip()
        editorial_valor = editorial.value.strip()
        anio_valor = anio.value.strip()

        if not titulo_valor or not autor_valor:
            mostrar_mensaje(
                "Complete los datos del libro."
            )
            return

        try:
            anio_valor = int(anio_valor)
        except ValueError:
            mostrar_mensaje(
                "El año debe ser numérico."
            )
            return

        actualizado = catalogo.actualizar_libro(
            codigo_valor,
            titulo_valor,
            autor_valor,
            editorial_valor,
            anio_valor
        )

        if actualizado:

            mostrar_mensaje(
                "Libro actualizado correctamente."
            )

            actualizar_tabla()

    # ==========================================
    # ELIMINAR
    # ==========================================

    def eliminar_click(e):

        codigo_valor = codigo.value.strip()

        if not codigo_valor:
            mostrar_mensaje(
                "Ingrese el código del libro."
            )
            return

        eliminado = catalogo.eliminar_libro(
            codigo_valor
        )

        if eliminado:

            mostrar_mensaje(
                "Libro eliminado correctamente."
            )

            limpiar_campos()
            actualizar_tabla()

        else:

            mostrar_mensaje(
                "El libro no existe."
            )

    # ==========================================
    # LIMPIAR
    # ==========================================

    def limpiar_click(e):

        limpiar_campos()

        mostrar_mensaje(
            "Campos limpiados."
        )

    # ==========================================
    # BOTONES
    # ==========================================

    boton_agregar = ft.ElevatedButton(
        text="Agregar",
        icon=ft.Icons.ADD,
        on_click=agregar_click
    )

    boton_buscar = ft.ElevatedButton(
        text="Buscar",
        icon=ft.Icons.SEARCH,
        on_click=buscar_click
    )

    boton_actualizar = ft.ElevatedButton(
        text="Actualizar",
        icon=ft.Icons.EDIT,
        on_click=actualizar_click
    )

    boton_eliminar = ft.ElevatedButton(
        text="Eliminar",
        icon=ft.Icons.DELETE,
        on_click=eliminar_click
    )

    boton_limpiar = ft.ElevatedButton(
        text="Limpiar",
        icon=ft.Icons.CLEAR,
        on_click=limpiar_click
    )

    # ==========================================
    # INTERFAZ
    # ==========================================

    page.add(

        ft.Text(
            "SISTEMA DE BIBLIOTECA",
            size=30,
            weight=ft.FontWeight.BOLD
        ),

        ft.Text(
            "SEMANA 6 - INTERFAZ GRÁFICA",
            size=22
        ),

        ft.Divider(),

        ft.Text(
            "CATÁLOGO DE LIBROS",
            size=24,
            weight=ft.FontWeight.BOLD
        ),

        ft.Row(
            [
                codigo,
                titulo
            ],
            wrap=True
        ),

        ft.Row(
            [
                autor,
                editorial
            ],
            wrap=True
        ),

        ft.Row(
            [
                anio,
                tipo
            ],
            wrap=True
        ),

        ft.Text(
            "Datos del libro físico",
            size=18,
            weight=ft.FontWeight.BOLD
        ),

        ft.Row(
            [
                ubicacion,
                paginas
            ],
            wrap=True
        ),

        ft.Text(
            "Datos del libro digital",
            size=18,
            weight=ft.FontWeight.BOLD
        ),

        ft.Row(
            [
                formato,
                tamano,
                url
            ],
            wrap=True
        ),

        ft.Divider(),

        ft.Text(
            "OPERACIONES CRUD",
            size=22,
            weight=ft.FontWeight.BOLD
        ),

        ft.Row(
            [
                boton_agregar,
                boton_buscar,
                boton_actualizar,
                boton_eliminar,
                boton_limpiar
            ],
            wrap=True
        ),

        ft.Divider(),

        mensaje,

        cantidad,

        ft.Text(
            "CATÁLOGO",
            size=22,
            weight=ft.FontWeight.BOLD
        ),

        ft.Row(
            [
                tabla
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )

    # ==========================================
    # DATOS INICIALES
    # ==========================================

    libro1 = LibroFisico(
        "L001",
        "Cien años de soledad",
        "Gabriel García Márquez",
        "Sudamericana",
        1967,
        "Estante A-10",
        471
    )

    libro2 = LibroDigital(
        "L002",
        "El principito",
        "Antoine de Saint-Exupéry",
        "Salamandra",
        1943,
        "PDF",
        2.5,
        "https://biblioteca.com/libro/L002"
    )

    catalogo.agregar_libro(libro1)
    catalogo.agregar_libro(libro2)

    actualizar_tabla()


ft.app(target= main)
