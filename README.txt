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
