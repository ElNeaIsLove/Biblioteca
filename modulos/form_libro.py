from PyQt5.QtWidgets import QMessageBox


class FormLibro:

    def guardar_libro(self):

        titulo = self.lineEdit_4.text().strip()

        if not titulo:

            QMessageBox.warning(
                self,
                "Error",
                "El título es obligatorio"
            )
            return

        if self.libro_actual_id is None:

            self.crud_libros.agregar(
                titulo,
                self.comboBox_3.currentData(),
                self.spinBox.value(),
                self.comboBox_4.currentData(),
                #self.comboBox_5.currentData()
            )

        else:

            self.crud_libros.modificar(
                self.libro_actual_id,
                titulo,
                self.comboBox_3.currentData(),
                self.spinBox.value(),
                self.comboBox_4.currentData(),
                #self.comboBox_5.currentData()
            )

        self.abrir_abm("libros")

    def cancelar_libro(self):

        self.abrir_abm("libros")

    def limpiar_form(self):

        self.lineEdit_4.clear()
        self.spinBox.setValue(2000)

        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        #self.comboBox_5.setCurrentIndex(0)