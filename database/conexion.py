import sqlite3
import os

class Conexion:

    def __init__(self):

        db = os.path.join(os.path.dirname(__file__), "..", "datos", "libros.sqlite3")

        self.con = sqlite3.connect(db)
        self.con.row_factory = sqlite3.Row

    def consultar(self, q, p=()):
        cur = self.con.cursor()
        cur.execute(q, p)
        return cur.fetchall()

    def ejecutar(self, q, p=()):
        cur = self.con.cursor()
        cur.execute(q, p)
        self.con.commit()