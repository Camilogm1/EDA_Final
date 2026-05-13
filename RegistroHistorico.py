class RegistroHistorico:
    """
    TDA que representa un registro histórico en el sistema AncestryDigital.
    """

    def __init__(self, id: int, nombre: str, anio: int, tipo_documento: str):
        self.id             = id
        self.nombre         = nombre
        self.anio           = anio
        self.tipo_documento = tipo_documento

    def __str__(self) -> str:
        return (f"[ID: {self.id} | Nombre: {self.nombre} "
                f"| Año: {self.anio} | Tipo: {self.tipo_documento}]")