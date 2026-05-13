from RegistroHistorico import RegistroHistorico


class NodoRegistro:
    """
    Nodo del Árbol Binario de Búsqueda.
    Contiene el dato y los punteros al hijo izquierdo y derecho.
    """

    def __init__(self, dato: RegistroHistorico):
        self.dato      = dato
        self.izquierdo = None
        self.derecho   = None