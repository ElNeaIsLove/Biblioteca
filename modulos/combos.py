class Combos:

    def cargar_autores(self):

        self.comboBox_3.clear()

        for a in self.crud_autores.listar():

            self.comboBox_3.addItem(
                a["nombre"],
                a["id"]
            )

    def cargar_categorias(self):

        self.comboBox_4.clear()

        for c in self.crud_categorias.listar():

            self.comboBox_4.addItem(
                c["nombre"],
                c["id"]
            )

    def cargar_estados(self):

        self.comboBox_5.clear()

        self.comboBox_5.addItem("Disponible", 1)
        self.comboBox_5.addItem("Prestado", 2)

    def cargar_grados(self):

        self.comboBox_9.clear()

        self.comboBox_9.addItem("1")
        self.comboBox_9.addItem("2")
        self.comboBox_9.addItem("3")
        self.comboBox_9.addItem("4")
        self.comboBox_9.addItem("5")
        self.comboBox_9.addItem("6")
        self.comboBox_9.addItem("7")

    def cargar_tipo(self):

        self.comboBox_6.clear()

        self.comboBox_6.addItem("Alumno")
        self.comboBox_6.addItem("Profesor")

    def cargar_combo_libros_prestamo(self):
        self.comboBox_8.clear()
    
        self.comboBox_8.addItem("Seleccione un libro", None)
    
        libros = self.crud_libros.listar_filtrado(estados=[1])
    
        for libro in libros:
            self.comboBox_8.addItem(
                f'{libro["titulo"]} ({libro["autor"]})',
                libro["id"]
            )
    
    
    def cargar_combo_personas_prestamo(self):
        self.comboBox_11.clear()
    
        self.comboBox_11.addItem("Seleccione una persona", None)
    
        for persona in self.crud_personas.listar():
            self.comboBox_11.addItem(
                persona["nombre"],
                persona["id"]
            )