class Navegacion:

    def volver_principal(self):
        self.stackedWidget.setCurrentIndex(0)
        self.configurar_tabla_libros_inicio()
        self.limpiar_filtros()

    def ir_menu_abm(self):
        self.stackedWidget.setCurrentIndex(1)

    def volver_menu_abm(self):
        self.stackedWidget.setCurrentIndex(1)

    def abrir_abm(self, modo):
    
        self.modo_abm = modo
    
        if modo == "libros":
            self.stackedWidget.setCurrentIndex(2)
            self.configurar_tabla_libros()
            self.cargar_tabla_libros()
    
        elif modo == "autores":
            self.stackedWidget.setCurrentIndex(2)
            self.configurar_tabla_autores()
            self.cargar_tabla_autores()
    
        elif modo == "categorias":
            self.stackedWidget.setCurrentIndex(2)
            self.configurar_tabla_categorias()
            self.cargar_tabla_categorias()
    
        elif modo == "personas":
            self.stackedWidget.setCurrentIndex(2)
            self.configurar_tabla_personas()
            self.cargar_tabla_personas()
    
        elif modo == "prestamos":
            self.stackedWidget.setCurrentIndex(6)
            self.configurar_tabla_prestamos()
            self.cargar_tabla_prestamos()   

        elif modo == "Estadísticas":
            self.stackedWidget.setCurrentIndex(7)
            self.configurar_tabla_prestamos()
            self.cargar_tabla_estadisticas() 