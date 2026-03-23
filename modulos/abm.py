from PyQt5.QtWidgets import QMessageBox
from dialogos.cuadro_dialogo import CuadroDeDialogo
from datetime import datetime


class ABM:

    def nuevo_item(self):
    
        if self.modo_abm == "libros":
    
            self.libro_actual_id = None
            self.limpiar_form()
            self.stackedWidget.setCurrentIndex(3)
            return
    
        elif self.modo_abm == "personas":
    
            self.persona_actual_id = None
            self.limpiar_form_persona()
            self.stackedWidget.setCurrentIndex(4)
            return
    
        elif self.modo_abm == "prestamos":
    
            self.prestamo_actual_id = None
            self.limpiar_form_prestamo()
            self.stackedWidget.setCurrentIndex(5)
            self.cargar_combo_libros_prestamo()
            self.cargar_combo_personas_prestamo()
            return

        dlg = CuadroDeDialogo("Nuevo")

        if dlg.exec_():

            if self.modo_abm == "autores":

                self.crud_autores.agregar(dlg.valor())
                self.cargar_tabla_autores()

            elif self.modo_abm == "categorias":

                self.crud_categorias.agregar(dlg.valor())
                self.cargar_tabla_categorias()

            self.cargar_autores()
            self.cargar_categorias()
            self.cargar_filtros()

    def modificar_item(self):

        fila = self.tableWidget.currentRow()

        if fila < 0:
            return

        item_id = int(self.tableWidget.item(fila, 0).text())
        nombre = self.tableWidget.item(fila, 1).text()

        if self.modo_abm == "libros":

            self.libro_actual_id = item_id
            libro = self.crud_libros.obtener(item_id)

            self.lineEdit_4.setText(libro["titulo"])
            self.spinBox.setValue(libro["anio"])

            self.comboBox_3.setCurrentIndex(
                self.comboBox_3.findData(libro["autor_id"])
            )

            self.comboBox_4.setCurrentIndex(
                self.comboBox_4.findData(libro["categoria_id"])
            )

            #self.comboBox_5.setCurrentIndex(
                #self.comboBox_5.findData(libro["estado_id"])
            #)

            self.stackedWidget.setCurrentIndex(3)
            return

        elif self.modo_abm == "personas":
            self.persona_actual_id = item_id
            persona = self.crud_personas.obtener(item_id)
            
            if persona is None:
                QMessageBox.warning(self, "Error", "No se encontró la persona")
                return
        
            # Cargar datos en el formulario
            self.lineEdit_5.setText(persona["nombre"])
            self.comboBox_6.setCurrentIndex(self.comboBox_6.findText(persona["tipo"]))
            self.comboBox_9.setCurrentIndex(self.comboBox_9.findText(persona["curso"]))
            self.lineEdit_6.setText(persona["email"] or "")
        
            self.stackedWidget.setCurrentIndex(4)
            return


        elif self.modo_abm == "prestamos":
            self.prestamo_actual_id = item_id
            prestamo = self.crud_prestamos.obtener(item_id)
        
        
            # Cargar datos en los combos
            self.comboBox_8.setCurrentIndex(
                self.comboBox_8.findData(prestamo["libro_id"])
            )
            self.comboBox_11.setCurrentIndex(
                self.comboBox_11.findData(prestamo["persona_id"])
            )
        
            self.stackedWidget.setCurrentIndex(7)
            return


        dlg = CuadroDeDialogo("Modificar", nombre)

        if dlg.exec_():

            if self.modo_abm == "autores":

                self.crud_autores.modificar(item_id, dlg.valor())
                self.cargar_tabla_autores()

            elif self.modo_abm == "categorias":

                self.crud_categorias.modificar(item_id, dlg.valor())
                self.cargar_tabla_categorias()

            self.cargar_autores()
            self.cargar_categorias()
            self.cargar_filtros()

    def eliminar_item(self):
    
        fila = self.tableWidget.currentRow()
    
        if fila < 0:
            return
    
        item_id = int(self.tableWidget.item(fila, 0).text())
    
        # Confirmación
        if QMessageBox.question(
                self,
                "Confirmar",
                "¿Está seguro que desea eliminar este elemento?"
        ) != QMessageBox.Yes:
            return
    
        # -------- LIBROS --------
        if self.modo_abm == "libros":
    
            if self.crud_libros.esta_prestado(item_id):
                QMessageBox.warning(
                    self,
                    "No permitido",
                    "El libro está prestado y no puede ser eliminado."
                )
                return
    
            self.crud_libros.eliminar(item_id)
            self.cargar_tabla_libros()
    
        # -------- AUTORES --------
        elif self.modo_abm == "autores":
    
            if self.crud_autores.tiene_libros(item_id):
                QMessageBox.warning(
                    self,
                    "No permitido",
                    "El autor tiene libros asociados y no puede ser eliminado."
                )
                return
    
            self.crud_autores.eliminar(item_id)
            self.cargar_tabla_autores()
    
        # -------- CATEGORIAS --------
        elif self.modo_abm == "categorias":
    
            if self.crud_categorias.tiene_libros(item_id):
                QMessageBox.warning(
                    self,
                    "No permitido",
                    "La categoría tiene libros asociados y no puede ser eliminada."
                )
                return
    
            self.crud_categorias.eliminar(item_id)
            self.cargar_tabla_categorias()
    
        # -------- PERSONAS --------
        elif self.modo_abm == "personas":
    
            if self.crud_personas.tiene_prestamos(item_id):
                QMessageBox.warning(
                    self,
                    "No permitido",
                    "La persona tiene préstamos asociados y no puede ser eliminada."
                )
                return
    
            self.crud_personas.eliminar(item_id)
            self.cargar_tabla_personas()
    
        # -------- PRESTAMOS --------
        elif self.modo_abm == "prestamos":
    
            self.crud_prestamos.eliminar(item_id)
            self.cargar_tabla_prestamos()
    
        # -------- REFRESCOS GENERALES --------
        self.cargar_autores()
        self.cargar_categorias()
        self.cargar_filtros()

    def devolver_prestamo(self):
        print("Hasta aca esta funcionando")
    
        seleccion = self.tableWidget_2.selectionModel().selectedRows()
    
        if not seleccion:
            QMessageBox.warning(self, "Error", "Seleccione un préstamo")
            return
    
        fila = seleccion[0].row()
    
        prestamo_id = int(self.tableWidget_2.item(fila, 0).text())
    
        print("ID:", prestamo_id)
    
        prestamo = self.crud_prestamos.obtener(prestamo_id)
    
        if prestamo["fecha_devolucion"] is not None:
            QMessageBox.information(self, "Info", "El préstamo ya fue devuelto.")
            return
    
        fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
    
        self.crud_prestamos.devolver(prestamo_id, fecha_devolucion)
    
        # recargar combo de libros disponibles
        self.cargar_combo_libros_prestamo()
    
        QMessageBox.information(self, "Devolución", "Préstamo devuelto correctamente")
    
        self.cargar_tabla_prestamos()   