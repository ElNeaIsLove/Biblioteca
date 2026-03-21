from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox
)


class CuadroDeDialogo(QDialog):
    def __init__(self, titulo, texto_inicial=""):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setModal(True)
        self.resize(320, 140)

        self.input = QLineEdit()
        self.input.setText(texto_inicial)
        self.input.setPlaceholderText("Ingrese nombre")

        btn_guardar = QPushButton("Guardar")
        btn_cancelar = QPushButton("Cancelar")

        btn_guardar.clicked.connect(self.validar)
        btn_cancelar.clicked.connect(self.reject)

        layout_botones = QHBoxLayout()
        layout_botones.addStretch()
        layout_botones.addWidget(btn_guardar)
        layout_botones.addWidget(btn_cancelar)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nombre"))
        layout.addWidget(self.input)
        layout.addLayout(layout_botones)

        self.setLayout(layout)

    def validar(self):
        if not self.valor():
            QMessageBox.warning(
                self,
                "Dato inválido",
                "El nombre no puede estar vacío."
            )
            return
        self.accept()

    def valor(self):
        return self.input.text().strip()