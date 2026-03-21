from PyQt5.QtWidgets import QMessageBox
from datetime import datetime


class FormPrestamo:

    def guardar_prestamo(self):
        libro_id = self.comboBox_8.currentData()
        persona_id = self.comboBox_11.currentData()

        if libro_id is None or persona_id is None:
            QMessageBox.warning(self, "Error", "Ambos campos son obligatorios")
            return

        # Validar si ya está prestado
        if self.crud_libros.esta_prestado(libro_id):
            QMessageBox.warning(self, "No permitido", "El libro ya está prestado")
            return

        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        if self.prestamo_actual_id is None:
            self.crud_prestamos.agregar(
                libro_id,
                persona_id,
                fecha_actual
            )
        else:
            self.crud_prestamos.modificar(
                self.prestamo_actual_id,
                libro_id,
                persona_id,
                fecha_actual
            )

        QMessageBox.information(self, "Éxito", "Préstamo guardado correctamente")

        self.abrir_abm("prestamos")

    def limpiar_form_prestamo(self):
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_11.setCurrentIndex(0)

    def cancelar_prestamo(self):
        self.limpiar_form_prestamo()
        self.abrir_abm("prestamos")