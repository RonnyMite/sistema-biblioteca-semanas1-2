# Sistema de Biblioteca

## Descripción

Sistema desarrollado en **Python** para representar el funcionamiento básico de una biblioteca mediante **Programación Orientada a Objetos (POO)**. Permite gestionar libros físicos y digitales, usuarios, préstamos y devoluciones.

## Objetivo

Aplicar los conceptos de programación estudiados hasta la **Semana 3**, construyendo una solución organizada en clases y módulos que permita representar de forma sencilla las operaciones principales de una biblioteca.

## Principales funcionalidades

- Registrar y consultar libros.
- Diferenciar libros físicos y digitales mediante herencia.
- Registrar estudiantes y docentes como tipos de usuarios.
- Realizar préstamos de libros disponibles.
- Cambiar el estado de un libro entre `DISPONIBLE` y `PRESTADO`.
- Registrar la fecha de inicio y devolución de un préstamo.
- Cerrar préstamos y devolver libros.
- Consultar libros, usuarios y préstamos registrados.
- Aplicar encapsulación mediante atributos privados y métodos getters/setters.
- Aplicar una clase abstracta `Cliente` y polimorfismo mediante clientes mayoristas y minoristas.
- Utilizar `Enum` para representar los estados de los libros.

## Estructura del proyecto

```text
sistema-biblioteca/
├── biblioteca.py
├── cliente.py
├── cliente_mayorista.py
├── cliente_minorista.py
├── docente.py
├── estudiante.py
├── libro.py
├── libro_digital.py
├── libro_fisico.py
├── prestamo.py
├── usuario.py
├── main.py
├── README.md
└── .gitignore
```

## Conceptos de POO aplicados

### Encapsulación

Los atributos de las clases se manejan como privados utilizando `__atributo` y se accede a ellos mediante métodos getters y setters.

### Herencia

- `LibroFisico` y `LibroDigital` heredan de `Libro`.
- `Estudiante` y `Docente` heredan de `Usuario`.
- `ClienteMayorista` y `ClienteMinorista` heredan de `Cliente`.

### Abstracción

`Cliente` es una clase abstracta que define el método `calcular_descuento()` que deben implementar sus clases hijas.

### Polimorfismo

`ClienteMayorista` y `ClienteMinorista` implementan el mismo método `calcular_descuento()` con comportamientos diferentes.

### Asociación y composición

`Prestamo` relaciona un libro con un usuario, mientras que `Biblioteca` administra sus colecciones de libros, usuarios y préstamos.

### Enumeración

`EstadoLibro` permite controlar los estados `DISPONIBLE` y `PRESTADO`.

## Requisitos

- Python 3.x
- No requiere librerías externas.

## Ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

Si en el equipo el comando anterior no funciona, también se puede probar:

```bash
python3 main.py
```

## Demostración

Al ejecutar `main.py`, el sistema crea una biblioteca, registra libros y usuarios, demuestra conceptos de herencia, realiza un préstamo, muestra el cambio de estado del libro y finalmente registra su devolución.


# Sistema de Biblioteca - Semanas 5 y 6

## Descripción

Este proyecto corresponde al desarrollo de un sistema de biblioteca
realizado en Python mediante programación orientada a objetos.

El proyecto integra los conocimientos desarrollados durante las
Semanas 1, 2, 3, 5 y 6.

## Semana 5

En la Semana 5 se implementó un catálogo de productos utilizando
diferentes colecciones de Python:

- list
- dict
- set

Estas colecciones permiten almacenar, buscar y administrar los
productos del catálogo.

## Semana 6

En la Semana 6 se desarrolló una interfaz gráfica utilizando Flet.

La aplicación permite realizar las siguientes operaciones:

- Crear productos
- Consultar productos
- Actualizar productos
- Eliminar productos
- Listar productos

También se implementó manejo de eventos mediante los botones de
la interfaz gráfica.

## Operaciones CRUD

### Crear

Permite agregar un nuevo producto al catálogo.

### Consultar

Permite buscar un producto utilizando su código.

### Actualizar

Permite modificar el nombre, precio y categoría de un producto.

### Eliminar

Permite eliminar un producto del catálogo.

### Listar

Permite visualizar todos los productos registrados.

## Validaciones

El sistema valida:

- Código obligatorio.
- Nombre obligatorio.
- Precio obligatorio.
- Precio numérico.
- Precio mayor que cero.
- Categoría obligatoria.
- Códigos duplicados.

## Estructura del proyecto

```text
biblioteca_semana1y2_archivos_py/
│
├── biblioteca.py
├── libro.py
├── libro_fisico.py
├── libro_digital.py
├── usuario.py
├── estudiante.py
├── docente.py
├── prestamo.py
│
├── cliente.py
├── cliente_mayorista.py
├── cliente_minorista.py
│
├── producto.py
├── catalogo.py
├── main_semana5.py
├── app.py
│
├── main.py
├── README.md
└── requirements.txt

