from database.conexion import Conexion
from database.crud_libros import CRUDLibros


class CRUDPrestamos:
    def __init__(self):
        self.db = Conexion()
        self.crud_libros = CRUDLibros()

    def listar(self):
        return self.db.consultar("""
            SELECT 
                p.id,
                l.titulo AS libro,
                pe.nombre,
                p.fecha_prestamo,
                p.fecha_devolucion
            FROM prestamos p
            JOIN libros l ON p.libro_id = l.id
            JOIN personas pe ON p.persona_id = pe.id
            ORDER BY p.fecha_prestamo DESC
        """)

    def listar_activos(self):
        return self.db.consultar("""
            SELECT p.id, l.titulo AS libro, pe.nombre, p.fecha_prestamo
            FROM prestamos p
            JOIN libros l ON p.libro_id = l.id
            JOIN personas pe ON p.persona_id = pe.id
            WHERE p.fecha_devolucion IS NULL
            ORDER BY p.fecha_prestamo
        """)

    def obtener(self, prestamo_id):
        r = self.db.consultar(
            "SELECT * FROM prestamos WHERE id=?",
            (prestamo_id,)
        )
        return r[0] if r else None

    def agregar(self, libro_id, persona_id, fecha):
        # 1. Insertar préstamo
        self.db.ejecutar(
            "INSERT INTO prestamos (libro_id, persona_id, fecha_prestamo) VALUES (?, ?, ?)",
            (libro_id, persona_id, fecha)
        )

        # 2. Marcar libro como prestado (reutilizando método)
        self.crud_libros.marcar_prestado(libro_id)

    def modificar(self, prestamo_id, libro_id, persona_id, fecha):
        #  Recomendación: no cambiar libro si ya está prestado
        prestamo_actual = self.obtener(prestamo_id)

        if prestamo_actual:
            libro_anterior = prestamo_actual["libro_id"]

            # Si cambió el libro
            if libro_anterior != libro_id:
                # liberar el anterior
                self.crud_libros.marcar_disponible(libro_anterior)

                # marcar el nuevo como prestado
                self.crud_libros.marcar_prestado(libro_id)

        self.db.ejecutar(
            "UPDATE prestamos SET libro_id=?, persona_id=?, fecha_prestamo=? WHERE id=?",
            (libro_id, persona_id, fecha, prestamo_id)
        )

    def devolver(self, prestamo_id, fecha):
        # Obtener préstamo
        prestamo = self.obtener(prestamo_id)

        if not prestamo:
            return

        # Si ya fue devuelto, no hacer nada
        if prestamo["fecha_devolucion"] is not None:
            return

        libro_id = prestamo["libro_id"]

        # 1. Registrar fecha de devolución
        self.db.ejecutar(
            "UPDATE prestamos SET fecha_devolucion=? WHERE id=?",
            (fecha, prestamo_id)
        )

        # 2. Marcar libro como disponible
        self.crud_libros.marcar_disponible(libro_id)

    def eliminar(self, prestamo_id):
        prestamo = self.obtener(prestamo_id)

        if not prestamo:
            return

        libro_id = prestamo["libro_id"]

        # Si no fue devuelto, liberar libro
        if prestamo["fecha_devolucion"] is None:
            self.crud_libros.marcar_disponible(libro_id)

        self.db.ejecutar(
            "DELETE FROM prestamos WHERE id=?",
            (prestamo_id,)
        )

    def estadisticas_libros(self, orden="DESC"):
        return self.db.consultar(f"""
            SELECT 
                l.titulo AS libro,
                COUNT(*) AS cantidad
            FROM prestamos p
            JOIN libros l ON p.libro_id = l.id
            GROUP BY l.titulo
            ORDER BY cantidad {orden}
        """)

    def estadisticas_personas(self):
        return self.db.consultar("""
            SELECT 
                pe.nombre,
                COUNT(*) AS cantidad
            FROM prestamos p
            JOIN personas pe ON p.persona_id = pe.id
            GROUP BY pe.nombre
            ORDER BY cantidad DESC
        """)