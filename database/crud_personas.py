from database.conexion import Conexion

class CRUDPersonas:
    def __init__(self):
        self.db = Conexion()

    def listar(self):
        return self.db.consultar(
            "SELECT id, nombre, tipo, curso, email FROM personas ORDER BY nombre"
        )

    def obtener(self, persona_id):
        r = self.db.consultar(
            "SELECT id, nombre, tipo, curso, email FROM personas WHERE id=?",
            (persona_id,)
        )
        return r[0] if r else None  # devuelve objeto compatible con ['campo']

    def agregar(self, nombre, tipo, curso, email=None):
        self.db.ejecutar(
            "INSERT INTO personas (nombre, tipo, curso, email) VALUES (?, ?, ?, ?)",
            (nombre, tipo, curso, email)
        )

    def modificar(self, persona_id, nombre, tipo, curso, email=None):
        self.db.ejecutar(
            "UPDATE personas SET nombre=?, tipo=?, curso=?, email=? WHERE id=?",
            (nombre, tipo, curso, email, persona_id)
        )

    def eliminar(self, persona_id):
        self.db.ejecutar("DELETE FROM personas WHERE id=?", (persona_id,))