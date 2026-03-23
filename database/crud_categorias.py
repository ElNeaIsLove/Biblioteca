from database.conexion import Conexion

class CRUDCategorias:
    def __init__(self):
        self.db = Conexion()

    def listar(self):
        return self.db.consultar("SELECT id, nombre FROM categorias ORDER BY nombre")

    def agregar(self, nombre):
        self.db.ejecutar("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))

    def modificar(self, id_, nombre):
        self.db.ejecutar("UPDATE categorias SET nombre=? WHERE id=?", (nombre, id_))

    def eliminar(self, id_):
        self.db.ejecutar("DELETE FROM categorias WHERE id=?", (id_,))

    def tiene_libros(self, categoria_id):
        consulta = "SELECT COUNT(*) FROM libros WHERE categoria_id = ?"
        resultado = self.db.consultar(consulta, (categoria_id,))
        return resultado[0][0] > 0