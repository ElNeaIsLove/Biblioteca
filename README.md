# Sistema de Gestión de Biblioteca

Aplicación de escritorio desarrollada en Python utilizando PyQt5 para la gestión de libros, autores, categorías, personas y préstamos.

## Requisitos

Antes de ejecutar el sistema, asegurarse de tener instalado:

* Python 3.10 o superior
* pip (gestor de paquetes de Python)

## Librerías necesarias

Instalar las siguientes dependencias:

```
pip install PyQt5
pip install pyqt5-tools
```

## Estructura del proyecto

El sistema está organizado en las siguientes carpetas y archivos:

* `main.py` → Punto de inicio de la aplicación
* `ventana_principal.py` → Ventana principal
* `modulos/` → Lógica de navegación, tablas, ABM, formularios y combos
* `database/` → Conexión y operaciones CRUD
* `ui/` → Archivos `.ui` diseñados con Qt Designer
* `dialogos/` → Ventanas emergentes
* `datos/` → Base de datos del sistema

## Interfaz gráfica

La interfaz fue diseñada con Qt Designer.

Para abrir y editar los archivos `.ui`:

```
pyqt5-tools designer
```

## Ejecución

Para iniciar la aplicación:

```
python main.py
```

## Base de datos

La base de datos se encuentra dentro de la carpeta `datos/`.

Asegurarse de que el archivo de base de datos exista y sea accesible antes de ejecutar el sistema.

## Funcionalidades principales

* Gestión de libros (alta, baja y modificación)
* Gestión de autores y categorías
* Gestión de personas
* Registro de préstamos
* Filtros y búsqueda en tiempo real
