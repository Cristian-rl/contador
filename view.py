from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)

class VistaContador(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

        self.setWindowTitle("Contador de Caracteres 😎")
        self.resize(400, 250)

        self.crear_widgets()

    def crear_widgets(self):
        self.label = QLabel("Escribe tu texto:")
        self.texto = QTextEdit()
        self.texto.setPlaceholderText("Escribe algo aquí...")

        self.resultado = QLabel("Caracteres: 0")
        self.resultado.setStyleSheet("font-weight: bold; font-size: 14px;")

        self.boton_contar = QPushButton("Contar")
        self.boton_limpiar = QPushButton("Limpiar")
        self.boton_limpiar.setStyleSheet("background-color: #7C28B0; color: white;")

        self.boton_contar.clicked.connect(self.analizar)
        self.boton_limpiar.clicked.connect(self.limpiar)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_contar)
        botones_layout.addWidget(self.boton_limpiar)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.label)
        layout_principal.addWidget(self.texto)
        layout_principal.addWidget(self.resultado)
        layout_principal.addLayout(botones_layout)

        self.setLayout(layout_principal)

    def analizar(self):
        texto = self.texto.toPlainText()
        if texto.strip():
            self.controlador.contar_texto(texto)
        else:
            QMessageBox.warning(self, "Error", "El campo de texto está vacío")

    def mostrar_resultado(self, cantidad):
        self.resultado.setText(f"Caracteres: {cantidad}")

    def limpiar(self):
        self.texto.clear()
        self.resultado.setText("Caracteres: 0")
