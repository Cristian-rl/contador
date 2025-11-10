import sys
from PySide6.QtWidgets import QApplication
from controller import Controlador

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = Controlador()
    controlador.iniciar()
    sys.exit(app.exec())
