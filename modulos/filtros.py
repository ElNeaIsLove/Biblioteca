class Filtros:

    def cargar_filtros(self):

        self.comboBox.clear()
        self.comboBox_2.clear()

        self.comboBox.addItem("Todos", None)

        for a in self.crud_autores.listar():
            self.comboBox.addItem(
                a["nombre"],
                a["id"]
            )

        self.comboBox_2.addItem("Todas", None)

        for c in self.crud_categorias.listar():
            self.comboBox_2.addItem(
                c["nombre"],
                c["id"]
            )

    def aplicar_filtros(self):

        autor = self.comboBox.currentData()
        categoria = self.comboBox_2.currentData()

        anio_desde = self.lineEdit_2.text().strip()
        anio_hasta = self.lineEdit_3.text().strip()

        anio_desde = int(anio_desde) if anio_desde else None
        anio_hasta = int(anio_hasta) if anio_hasta else None

        estados = []

        if self.checkBox.isChecked():
            estados.append(1)

        if self.checkBox_2.isChecked():
            estados.append(2)

        libros = self.crud_libros.listar_filtrado(
            autor_id=autor,
            categoria_id=categoria,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
            estados=estados if estados else None
        )

        self.cargar_tabla(libros)

    def limpiar_filtros(self):

        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)

        self.cargar_tabla(self.crud_libros.listar())

    def buscar_en_vivo(self, texto):

        texto = texto.lower().strip()

        libros = self.crud_libros.listar()

        if texto:

            libros = [
                l for l in libros
                if texto in l["titulo"].lower()
                or texto in l["autor"].lower()
                or texto in l["categoria"].lower()
            ]

        self.cargar_tabla(libros)