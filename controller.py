from model import ContadorCaracteres
from view import VistaContador

class Controlador:
    def __init__(self):
        self.modelo = ContadorCaracteres()
        self.vista = VistaContador(self)

    def contar_texto(self, texto):
        cantidad = self.modelo.contar(texto)
        self.vista.mostrar_resultado(cantidad)

    def iniciar(self):
        self.vista.show()
