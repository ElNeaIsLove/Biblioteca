import sqlite3
import os

class Conexion:

    def __init__(self):

        db = os.path.join(os.path.dirname(__file__), "..", "datos", "libros.sqlite3")

        crear_db = not os.path.exists(db)

        self.con = sqlite3.connect(db)
        self.con.row_factory = sqlite3.Row

        # Activar claves foráneas
        self.con.execute("PRAGMA foreign_keys = ON")

        if crear_db:
            self._crear_tablas()

    def consultar(self, q, p=()):
        cur = self.con.cursor()
        cur.execute(q, p)
        return cur.fetchall()

    def ejecutar(self, q, p=()):
        cur = self.con.cursor()
        cur.execute(q, p)
        self.con.commit()

    def _crear_tablas(self):
        cur = self.con.cursor()

        cur.executescript("""

        CREATE TABLE autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        );

        CREATE TABLE categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        );

        CREATE TABLE estado (
            id INTEGER PRIMARY KEY,
            estado TEXT NOT NULL
        );

        CREATE TABLE libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER,
            autor_id INTEGER,
            categoria_id INTEGER,
            estado_id INTEGER DEFAULT 1,

            FOREIGN KEY (autor_id) REFERENCES autores(id),
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (estado_id) REFERENCES estado(id)
        );

        CREATE TABLE personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT,
            curso TEXT,
            email TEXT
        );

        CREATE TABLE prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            libro_id INTEGER NOT NULL,
            persona_id INTEGER NOT NULL,
            fecha_prestamo TEXT NOT NULL,
            fecha_devolucion TEXT,

            FOREIGN KEY (libro_id) REFERENCES libros(id),
            FOREIGN KEY (persona_id) REFERENCES personas(id)
        );

        """)

        # Insertar estados iniciales
        cur.executemany(
            "INSERT INTO estado (id, estado) VALUES (?, ?)",
            [
                (1, "Disponible"),
                (2, "Prestado")
            ]
        )

        self.con.commit()