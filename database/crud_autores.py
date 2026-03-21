from database.conexion import Conexion

class CRUDAutores:
    def __init__(self):
        self.db = Conexion()

    def listar(self):
        return self.db.consultar("SELECT id, nombre FROM autores ORDER BY nombre")

    def agregar(self, nombre):
        self.db.ejecutar("INSERT INTO autores (nombre) VALUES (?)", (nombre,))

    def modificar(self, id_, nombre):
        self.db.ejecutar("UPDATE autores SET nombre=? WHERE id=?", (nombre, id_))

    def eliminar(self, id_):
        self.db.ejecutar("DELETE FROM autores WHERE id=?", (id_,))