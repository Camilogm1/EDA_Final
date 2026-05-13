from NodoRegistro import NodoRegistro
from RegistroHistorico import RegistroHistorico


class ArbolHistorico:
    """
    Implementación manual de un Árbol Binario de Búsqueda (BST).
    Organiza los registros históricos por ID.
    NO usa sorted(), bisect, SortedList ni ninguna colección
    que gestione orden automáticamente.
    """

    def __init__(self):
        self._raiz = None

    # =========================================================
    # INSERCIÓN
    # =========================================================
    def insertar(self, registro: RegistroHistorico) -> bool:
        """Método público: inserta un registro. Retorna True si se insertó, False si el ID ya existe."""
        resultado = self._insertar_rec(self._raiz, registro)
        if resultado is None:
            return False          # ID duplicado, no se insertó
        self._raiz = resultado
        return True

    def _insertar_rec(self, nodo, registro):
        """
        Método privado recursivo: retorna None si el ID ya existe,
        o el nodo actualizado si la inserción fue exitosa.
        """
        if nodo is None:
            return NodoRegistro(registro)

        if registro.id < nodo.dato.id:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, registro)
        elif registro.id > nodo.dato.id:
            nodo.derecho = self._insertar_rec(nodo.derecho, registro)
        else:
            return None           # ID duplicado → señal de rechazo

        return nodo

    # =========================================================
    # BÚSQUEDA — O(log n) en árbol balanceado
    # =========================================================

    def buscar(self, id: int):
        """
        Método público: busca un registro por su ID.
        Retorna el RegistroHistorico encontrado, o None si no existe.
        """
        resultado = self._buscar_rec(self._raiz, id)
        return resultado.dato if resultado is not None else None


    def _buscar_rec(self, nodo, id: int):
        """
        Método privado recursivo: descarta la mitad del árbol en
        cada llamada gracias a la propiedad BST.
        """
        if nodo is None or nodo.dato.id == id:
            return nodo

        if id < nodo.dato.id:
            return self._buscar_rec(nodo.izquierdo, id)
        else:
            return self._buscar_rec(nodo.derecho, id)

    # =========================================================
    # ELIMINACIÓN — 3 casos
    # =========================================================

    def eliminar(self, id: int) -> None:
        """Método público: elimina el nodo con el ID dado."""
        if self.buscar(id) is None:
            print(f"⚠  No existe un registro con ID {id}")
            return
        self._raiz = self._eliminar_rec(self._raiz, id)
        print(f"✔  Registro con ID {id} eliminado correctamente.")

    def _eliminar_rec(self, nodo, id: int):
        """
        Método privado recursivo que maneja los 3 casos:
        CASO 1 — Nodo hoja: se elimina directamente.
        CASO 2 — Un hijo: el hijo reemplaza al nodo eliminado.
        CASO 3 — Dos hijos: se usa el SUCESOR IN-ORDER
                 (menor ID del subárbol derecho).
        """
        if nodo is None:
            return None

        if id < nodo.dato.id:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, id)
        elif id > nodo.dato.id:
            nodo.derecho = self._eliminar_rec(nodo.derecho, id)
        else:
            # CASO 1: Nodo hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            # CASO 2a: Solo hijo derecho
            if nodo.izquierdo is None:
                return nodo.derecho

            # CASO 2b: Solo hijo izquierdo
            if nodo.derecho is None:
                return nodo.izquierdo

            # CASO 3: Dos hijos → sucesor in-order
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.dato.id)

        return nodo

    def _encontrar_minimo(self, nodo):
        """Retorna el nodo con el ID mínimo del subárbol."""
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    # =========================================================
    # RECORRIDOS
    # =========================================================

    def recorrido_in_orden(self) -> None:
        """In-orden: Izquierdo → Raíz → Derecho (ordenado por ID)"""
        print("\n📋 Recorrido In-Orden (ordenado por ID):")
        self._in_orden_rec(self._raiz)
        print()

    def _in_orden_rec(self, nodo) -> None:
        if nodo is not None:
            self._in_orden_rec(nodo.izquierdo)
            print(f"  {nodo.dato}")
            self._in_orden_rec(nodo.derecho)

    def recorrido_pre_orden(self) -> None:
        """Pre-orden: Raíz → Izquierdo → Derecho"""
        print("\n📋 Recorrido Pre-Orden:")
        self._pre_orden_rec(self._raiz)
        print()

    def _pre_orden_rec(self, nodo) -> None:
        if nodo is not None:
            print(f"  {nodo.dato}")
            self._pre_orden_rec(nodo.izquierdo)
            self._pre_orden_rec(nodo.derecho)

    def recorrido_post_orden(self) -> None:
        """Post-orden: Izquierdo → Derecho → Raíz"""
        print("\n📋 Recorrido Post-Orden:")
        self._post_orden_rec(self._raiz)
        print()

    def _post_orden_rec(self, nodo) -> None:
        if nodo is not None:
            self._post_orden_rec(nodo.izquierdo)
            self._post_orden_rec(nodo.derecho)
            print(f"  {nodo.dato}")

    # =========================================================
    # ESTADÍSTICAS
    # =========================================================

    def altura(self) -> int:
        """Método público: retorna la altura del árbol."""
        return self._altura_rec(self._raiz)

    def _altura_rec(self, nodo) -> int:
        """
        Método privado recursivo: altura = máximo entre
        subárbol izquierdo y derecho, más 1.
        """
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo),
                       self._altura_rec(nodo.derecho))

    def contar_nodos(self) -> int:
        """Método público: retorna el total de nodos."""
        return self._contar_nodos_rec(self._raiz)

    def _contar_nodos_rec(self, nodo) -> int:
        """Método privado recursivo: cuenta todos los nodos."""
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_rec(nodo.izquierdo) \
                 + self._contar_nodos_rec(nodo.derecho)

    def esta_vacio(self) -> bool:
        """Verifica si el árbol está vacío."""
        return self._raiz is None