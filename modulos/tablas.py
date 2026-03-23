from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QTableWidget

class Tablas:

    def configurar_tabla_libros_inicio(self):
        self.Lista.horizontalHeader().setStretchLastSection(True)
        self.Lista.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        

    def configurar_tabla_libros(self):

        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)

        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Título", "Autor", "Año", "Categoría", "Estado"]
        )
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnHidden(0, True)  # Oculta la columna ID
        
    def configurar_tabla_autores(self):

        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Autor"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnHidden(0, True)  # Oculta la columna ID

    def configurar_tabla_categorias(self):

        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Categoría"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnHidden(0, True)  # Oculta la columna ID

    def configurar_tabla_personas(self):
    
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(5)
    
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID","Nombre", "Tipo", "Curso", "Email"]
        )
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnHidden(0, True)  # Oculta la columna ID

    def configurar_tabla_prestamos(self):
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setHorizontalHeaderLabels(
            ["ID", "Libro", "Persona", "Fecha préstamo", "Fecha devolución"]
        )
        self.tableWidget_2.setRowCount(0)  # limpia solo las filas, no los headers
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.setColumnHidden(0, True)  # Oculta la columna ID

        self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget_2.setSelectionMode(QTableWidget.SingleSelection)

        for p in self.crud_prestamos.listar():
            print(dict(p))    

    def configurar_tabla_estadisticas_libros(self):
       self.tableWidget_3.setColumnCount(2)
       self.tableWidget_3.setHorizontalHeaderLabels(
           ["Libro", "Cantidad de veces prestado"]
       )
       self.tableWidget_3.setRowCount(0)

       self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
       self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def configurar_tabla_estadisticas_personas(self):
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setHorizontalHeaderLabels(
            ["Nombre", "Cantidad de veces que pidió un libro"]
        )
        self.tableWidget_3.setRowCount(0)
    
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
  


    def cargar_tabla_libros(self):

        self.tableWidget.setRowCount(0)

        for i, l in enumerate(self.crud_libros.listar()):

            self.tableWidget.insertRow(i)

            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(l["id"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(l["titulo"]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(l["autor"]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(l["anio"])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(l["categoria"]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(l["estado"]))

    def cargar_tabla_autores(self):

        self.tableWidget.setRowCount(0)

        for i, a in enumerate(self.crud_autores.listar()):

            self.tableWidget.insertRow(i)

            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(a["id"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(a["nombre"]))

    def cargar_tabla_categorias(self):

        self.tableWidget.setRowCount(0)

        for i, c in enumerate(self.crud_categorias.listar()):

            self.tableWidget.insertRow(i)

            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(c["id"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(c["nombre"]))

    def cargar_tabla(self, libros):

        self.Lista.setRowCount(0)

        for i, l in enumerate(libros):

            self.Lista.insertRow(i)

            #self.Lista.setItem(i, 0, QTableWidgetItem(l["id"]))
            self.Lista.setItem(i, 0, QTableWidgetItem(l["titulo"]))
            self.Lista.setItem(i, 1, QTableWidgetItem(l["autor"]))
            self.Lista.setItem(i, 2, QTableWidgetItem(str(l["anio"])))
            self.Lista.setItem(i, 3, QTableWidgetItem(l["categoria"]))
            self.Lista.setItem(i, 4, QTableWidgetItem(l["estado"]))

    
    def cargar_tabla_personas(self):
    
        self.tableWidget.setRowCount(0)
    
        for i, p in enumerate(self.crud_personas.listar()):
    
            self.tableWidget.insertRow(i)
    
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(p["id"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(p["nombre"]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(p["tipo"]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(p["curso"]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(p["email"]))

    def cargar_tabla_prestamos(self):
        self.tableWidget_2.setRowCount(0)
    
        for i, p in enumerate(self.crud_prestamos.listar()):
            self.tableWidget_2.insertRow(i)

            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(p["id"])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(p["libro"]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(p["nombre"]))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(p["fecha_prestamo"]))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(p["fecha_devolucion"]))
    
    def cargar_tabla_estadisticas(self):
        self.tableWidget_3.setRowCount(0)
    
        opcion = self.comboBox_7.currentText()
    
        # OPCIÓN INICIAL
        if opcion == "Seleccione la estadistica que desea ver":
            self.Tetolo.setText("Estadísticas")
            self.tableWidget_3.setColumnCount(1)
            self.tableWidget_3.setHorizontalHeaderLabels(["Estadísticas"])
            self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
            self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            return
    
        # LIBROS MÁS PRESTADOS
        elif opcion == "Libros más prestados":
            self.Tetolo.setText("Estadísticas de libros más prestados")
            self.configurar_tabla_estadisticas_libros()
            datos = self.crud_prestamos.estadisticas_libros("DESC")
    
        # LIBROS MENOS PRESTADOS
        elif opcion == "Libros menos prestados":
            self.Tetolo.setText("Estadísticas de libros menos prestados")
            self.configurar_tabla_estadisticas_libros()
            datos = self.crud_prestamos.estadisticas_libros("ASC")
    
        # PERSONAS
        elif opcion == "Persona que más pide":
            self.Tetolo.setText("Personas que más solicitan préstamos")
            self.configurar_tabla_estadisticas_personas()
            datos = self.crud_prestamos.estadisticas_personas()
    
        else:
            return
    
        # CARGAR DATOS EN TABLA
        for i, p in enumerate(datos):
            self.tableWidget_3.insertRow(i)
        
            # Si es libro
            if "libro" in p.keys():
                nombre = p["libro"]
            # Si es persona
            elif "nombre" in p.keys():
                nombre = p["nombre"]
            else:
                nombre = "N/D"
        
            cantidad = str(p["cantidad"])  # accedé directo, no get()
        
            self.tableWidget_3.setItem(i, 0, QTableWidgetItem(nombre))
            self.tableWidget_3.setItem(i, 1, QTableWidgetItem(cantidad))        