class FormEstadisticas:
    def actualizar_estadisticas(self, opcion):
        """
        Solo maneja validación del combo y cambio de título.
        La carga de datos va en Tablas.
        """
        # OPCIÓN INICIAL
        if opcion == "Seleccione la estadistica que desea ver":
            self.Tetolo.setText("Estadísticas")
            # Limpiar tabla si querés
            self.tableWidget_3.setRowCount(0)
            return

        # Libros más prestados
        elif opcion == "Libros más prestados":
            self.Tetolo.setText("Estadísticas de libros más prestados")

        # Libros menos prestados
        elif opcion == "Libros menos prestados":
            self.Tetolo.setText("Estadísticas de libros menos prestados")

        # Personas que más piden
        elif opcion == "Persona que más pide":
            self.Tetolo.setText("Personas que más solicitan préstamos")

        # Llamar a la carga de datos en Tablas
        self.cargar_tabla_estadisticas(opcion)