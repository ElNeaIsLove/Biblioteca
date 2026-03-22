from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator

from database.crud_personas import CRUDPersonas
from database.crud_autores import CRUDAutores
from database.crud_categorias import CRUDCategorias
from database.conexion import Conexion
from database.crud_prestamos import CRUDPrestamos
from database.crud_libros import CRUDLibros

from modulos.navegacion import Navegacion
from modulos.filtros import Filtros
from modulos.tablas import Tablas
from modulos.abm import ABM
from modulos.form_libro import FormLibro
from modulos.combos import Combos
from modulos.form_personas import FormPersona
from modulos.form_prestamo import FormPrestamo


class MainWindow(QtWidgets.QMainWindow,
                 Navegacion,
                 Filtros,
                 Tablas,
                 ABM,
                 FormLibro,
                 FormPersona,
                 FormPrestamo,
                 Combos):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)

        self.crud_personas = CRUDPersonas()
        self.crud_autores = CRUDAutores()
        self.crud_categorias = CRUDCategorias()
        self.crud_libros = CRUDLibros()
        self.crud_prestamos = CRUDPrestamos()


        self.modo_abm = None
        self.libro_actual_id = None

        # VALIDADORES
        validador_anio = QIntValidator(1800, 2100, self)
        self.lineEdit_2.setValidator(validador_anio)
        self.lineEdit_3.setValidator(validador_anio)

        # PAGINA PRINCIPAL
        self.pushButton.clicked.connect(self.ir_menu_abm)
        self.pushButton_2.clicked.connect(self.aplicar_filtros)
        self.pushButton_3.clicked.connect(self.limpiar_filtros)
        self.lineEdit.textChanged.connect(self.buscar_en_vivo)

        # MENU ABM
        self.pushButton_4.clicked.connect(lambda: self.abrir_abm("libros"))
        self.pushButton_6.clicked.connect(lambda: self.abrir_abm("autores"))
        self.pushButton_5.clicked.connect(lambda: self.abrir_abm("categorias"))
        self.pushButton_18.clicked.connect(lambda: self.abrir_abm("personas"))
        self.pushButton_19.clicked.connect(lambda: self.abrir_abm("prestamos"))
        self.pushButton_24.clicked.connect(lambda: self.abrir_abm("Estadísticas"))
        self.pushButton_18.clicked.connect(lambda: print("personas"))
        self.pushButton_19.clicked.connect(lambda: print("prestamos"))
        self.pushButton_10.clicked.connect(self.volver_principal)

        # BOTONES ABM
        self.pushButton_8.clicked.connect(self.nuevo_item)
        self.pushButton_9.clicked.connect(self.modificar_item)
        self.pushButton_7.clicked.connect(self.eliminar_item)
        self.pushButton_11.clicked.connect(self.volver_menu_abm)

        # FORM LIBRO
        self.pushButton_12.clicked.connect(self.guardar_libro)
        self.pushButton_13.clicked.connect(self.cancelar_libro)
        self.pushButton_14.clicked.connect(self.cancelar_libro)

        # FORM LIBRO
        self.pushButton_15.clicked.connect(self.guardar_persona)
        self.pushButton_16.clicked.connect(self.limpiar_form_persona)
        self.pushButton_17.clicked.connect(self.cancelar_persona)

        # PRESTOAMOS
        self.pushButton_20.clicked.connect(self.guardar_prestamo)
        self.pushButton_23.clicked.connect(self.nuevo_item)
        self.pushButton_25.clicked.connect(self.devolver_prestamo)
        self.pushButton_26.clicked.connect(self.volver_menu_abm)

        # Estadísticas
        self.pushButton_27.clicked.connect(self.volver_menu_abm)

        # Prstamos
        self.pushButton_21.clicked.connect(lambda: self.abrir_abm("prestamos"))     

        # CARGAS
        self.cargar_autores()
        self.cargar_categorias()
        #self.cargar_estados()
        self.cargar_filtros()
        self.cargar_grados()
        self.cargar_tipo()

        self.cargar_combo_estadisticas()
        self.comboBox_7.currentIndexChanged.connect(self.cargar_tabla_estadisticas)

        self.volver_principal()

        print("Total de páginas:", self.stackedWidget.count())