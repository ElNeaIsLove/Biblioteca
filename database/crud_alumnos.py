from database.conexion import Conexion

class CRUDAlumnos:
    def __init__(self):
        self.db = Conexion()

    def listar(self):
        return self.db.consultar("SELECT id, nombre, curso, email FROM alumnos ORDER BY nombre")

    def agregar(self, nombre, curso, email):
        self.db.ejecutar(
            "INSERT INTO alumnos (nombre, curso, email) VALUES (?, ?, ?)",
            (nombre, curso, email)
        )

    def modificar(self, id_, nombre, curso, email):
        self.db.ejecutar(
            "UPDATE alumnos SET nombre=?, curso=?, email=? WHERE id=?",
            (nombre, curso, email, id_)
        )

    def eliminar(self, id_):
        self.db.ejecutar("DELETE FROM alumnos WHERE id=?", (id_,))