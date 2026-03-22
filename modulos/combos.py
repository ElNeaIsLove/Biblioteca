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
        self.comboBox_9.addItem("Seleccione un grado", None)
        self.comboBox_9.addItem("1ro")
        self.comboBox_9.addItem("2do")
        self.comboBox_9.addItem("3ro")
        self.comboBox_9.addItem("4to")
        self.comboBox_9.addItem("5to")
        self.comboBox_9.addItem("6to")
        self.comboBox_9.addItem("7mo")

    def cargar_tipo(self):

        self.comboBox_6.clear()
        self.comboBox_6.addItem("Seleccione un tipo", None)
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

    def cargar_combo_estadisticas(self):
        self.comboBox_7.clear()

        self.comboBox_7.addItem("Seleccione la estadistica que desea ver", None)
        self.comboBox_7.addItem("Libros más prestados")
        self.comboBox_7.addItem("Libros menos prestados")
        self.comboBox_7.addItem("Persona que más pide")
