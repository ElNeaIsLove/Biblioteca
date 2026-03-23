from database.conexion import Conexion

# Constantes para los estados
ESTADO_DISPONIBLE = 1
ESTADO_PRESTADO = 2

class CRUDLibros:
    def __init__(self):
        self.db = Conexion()

    def listar(self):
        return self.db.consultar("""
            SELECT l.id, l.titulo, a.nombre AS autor, l.anio,
                   c.nombre AS categoria, e.estado
            FROM libros l
            JOIN autores a ON l.autor_id = a.id
            JOIN categorias c ON l.categoria_id = c.id
            JOIN estado e ON l.estado_id = e.id
            ORDER BY l.titulo
        """)

    def listar_filtrado(self, autor_id=None, categoria_id=None, anio_desde=None, anio_hasta=None, estados=None):
        q = """
            SELECT l.id, l.titulo, a.nombre AS autor, l.anio,
                   c.nombre AS categoria, e.estado
            FROM libros l
            JOIN autores a ON l.autor_id = a.id
            JOIN categorias c ON l.categoria_id = c.id
            JOIN estado e ON l.estado_id = e.id
            WHERE 1=1
        """
        p = []

        if autor_id is not None:
            q += " AND l.autor_id=?"
            p.append(autor_id)
        if categoria_id is not None:
            q += " AND l.categoria_id=?"
            p.append(categoria_id)
        if anio_desde is not None:
            q += " AND l.anio >= ?"
            p.append(anio_desde)
        if anio_hasta is not None:
            q += " AND l.anio <= ?"
            p.append(anio_hasta)
        if estados:
            placeholders = ",".join("?" * len(estados))
            q += f" AND l.estado_id IN ({placeholders})"
            p.extend(estados)

        q += " ORDER BY l.titulo"
        return self.db.consultar(q, p)

    def obtener(self, libro_id):
        r = self.db.consultar("SELECT * FROM libros WHERE id=?", (libro_id,))
        return r[0] if r else None

    def esta_prestado(self, libro_id):
        r = self.db.consultar("SELECT 1 FROM libros WHERE id=? AND estado_id=?", (libro_id, ESTADO_PRESTADO))
        return bool(r)

    def agregar(self, titulo, autor_id, anio, categoria_id, estado=ESTADO_DISPONIBLE):
        self.db.ejecutar(
            "INSERT INTO libros (titulo, autor_id, anio, categoria_id, estado_id) VALUES (?, ?, ?, ?, ?)",
            (titulo, autor_id, anio, categoria_id, estado)
        )

    def modificar(self, libro_id, titulo, autor_id, anio, categoria_id):
        # Solo modifica los datos principales, no el estado
        self.db.ejecutar(
            "UPDATE libros SET titulo=?, autor_id=?, anio=?, categoria_id=? WHERE id=?",
            (titulo, autor_id, anio, categoria_id, libro_id)
        )

    def eliminar(self, libro_id):
        self.db.ejecutar("DELETE FROM libros WHERE id=?", (libro_id,))

    def marcar_prestado(self, libro_id):
        self.db.ejecutar("UPDATE libros SET estado_id=? WHERE id=?", (ESTADO_PRESTADO, libro_id))
    
    def marcar_disponible(self, libro_id):
        self.db.ejecutar("UPDATE libros SET estado_id=? WHERE id=?", (ESTADO_DISPONIBLE, libro_id))