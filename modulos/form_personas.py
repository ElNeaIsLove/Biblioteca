from PyQt5.QtWidgets import QMessageBox

class FormPersona:

    def guardar_persona(self):

        # Obtenemos los valores del formulario
        nombre = self.lineEdit_5.text().strip()
        tipo = self.comboBox_6.currentText().strip()
        curso = self.comboBox_9.currentText().strip()
        email = self.lineEdit_6.text().strip()  # opcional

        # Validamos campos obligatorios
        if not nombre or not tipo or not curso:
            QMessageBox.warning(
                self,
                "Error",
                "Nombre, Tipo y Curso son obligatorios"
            )
            return

        if self.persona_actual_id is None:
            # Nuevo registro
            self.crud_personas.agregar(
                nombre,
                tipo,
                curso,
                email
            )
        else:
            # Modificación de un registro existente
            self.crud_personas.modificar(
                self.persona_actual_id,
                nombre,
                tipo,
                curso,
                email
            )

        # Volvemos al ABM de personas
        self.abrir_abm("personas")

    def cancelar_persona(self):
        self.abrir_abm("personas")

    def limpiar_form_persona(self):
        self.lineEdit_5.clear()
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_9.setCurrentIndex(0)
        self.lineEdit_6.clear()  # opcional