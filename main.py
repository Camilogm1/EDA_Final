from ArbolHistorico import ArbolHistorico
from RegistroHistorico import RegistroHistorico


def mostrar_menu() -> None:
    print("\n")
    print("      ANCESTRYDIGITAL — MENÚ         ")
    print("══════════════════════════════════════")
    print("  1. Insertar registro                ")
    print("  2. Buscar registro por ID           ")
    print("  3. Eliminar registro por ID         ")
    print("  4. Recorrido In-Orden               ")
    print("  5. Recorrido Pre-Orden              ")
    print("  6. Recorrido Post-Orden             ")
    print("  7. Estadísticas del árbol           ")
    print("  0. Salir                            ")
    print("══════════════════════════════════════")

"""desiciones de diseño"""
def pausar() -> None:
    input("\n  Presione Enter para continuar...")


def pedir_id() -> int:
    """Solicita un ID válido (entero positivo)."""
    id_r = int(input("  ID: "))
    if id_r <= 0:
        raise ValueError("El ID debe ser un número entero positivo (mayor a 0).")
    return id_r


def pedir_año() -> int:
    """Solicita un año válido (entero positivo)."""
    anio = int(input("  Año: "))
    if anio <= 0:
        raise ValueError("El año debe ser un número entero positivo (mayor a 0).")
    return anio


def main() -> None:
    arbol = ArbolHistorico()

    
    arbol.insertar(RegistroHistorico(50, "Acta Fundacional Medellín",    1675, "Acta"))
    arbol.insertar(RegistroHistorico(30, "Carta Gobernación Antioquia",  1813, "Carta"))
    arbol.insertar(RegistroHistorico(70, "Escritura Hacienda El Retiro", 1890, "Escritura"))
    arbol.insertar(RegistroHistorico(20, "Bautismo Gregorio Gutiérrez",  1801, "Registro Civil"))
    arbol.insertar(RegistroHistorico(40, "Matrimonio Familia Ospina",    1856, "Registro Civil"))
    arbol.insertar(RegistroHistorico(60, "Defunción Juan de Dios Uribe", 1900, "Registro Civil"))
    arbol.insertar(RegistroHistorico(80, "Testamento Tomás Cipriano",    1862, "Testamento"))

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                id_r = pedir_id()
                nom  = input("  Nombre: ")
                if not nom.strip():
                    raise ValueError("El nombre no puede estar vacío.")
                anio = pedir_año()
                tipo = input("  Tipo de documento: ")
                if not tipo.strip():
                    raise ValueError("El tipo de documento no puede estar vacío.")
                
                if arbol.insertar(RegistroHistorico(id_r, nom, anio, tipo)):
                    print("Registro insertado correctamente.")
                else:
                    print(f"Ya existe un registro con ID {id_r}. No se almacenó.")
            except ValueError as e:
                print(f"Dato inválido: {e}")
            pausar()

        elif opcion == "2":
            try:
                id_b = int(input("  ID a buscar: "))
                if id_b <= 0:
                    raise ValueError("El ID debe ser un número entero positivo.")
                reg = arbol.buscar(id_b)
                if reg:
                    print(f"Encontrado: {reg}")
                else:
                    print(f"No existe registro con ID {id_b}")
            except ValueError as e:
                print(f" Dato inválido: {e}")
            pausar()

        elif opcion == "3":
            try:
                id_e = int(input("  ID a eliminar: "))
                if id_e <= 0:
                    raise ValueError("El ID debe ser un número entero positivo.")
                arbol.eliminar(id_e)
            except ValueError as e:
                print(f"Dato inválido: {e}")
            pausar()

        elif opcion == "4":
            arbol.recorrido_in_orden()
            pausar()

        elif opcion == "5":
            arbol.recorrido_pre_orden()
            pausar()

        elif opcion == "6":
            arbol.recorrido_post_orden()
            pausar()

        elif opcion == "7":
            print("\n Estadísticas del árbol:")
            print(f"  Total de nodos : {arbol.contar_nodos()}")
            print(f"  Altura del árbol: {arbol.altura()}")
            pausar()

        elif opcion == "0":
            print(" Cerrando AncestryDigital...")
            break

        else:
            print("Opción no válida.")
            pausar()


if __name__ == "__main__":
    main()