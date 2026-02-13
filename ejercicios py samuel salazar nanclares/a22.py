#22. Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.
def a22():
         try:
             inventario_inicial = int(input("Ingrese la cantidad inicial en inventario: "))
             cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
             cantidad_recibida = int(input("Ingrese la cantidad recibida: "))

             inventario_final = inventario_inicial - cantidad_vendida + cantidad_recibida

             print(f"\n{'MOVIMIENTO DE INVENTARIO'}")
             print(f"Inventario inicial: {inventario_inicial} unidades")
             print(f"Cantidad vendida: -{cantidad_vendida} unidades")
             print(f"Cantidad recibida: +{cantidad_recibida} unidades")
             print(f"INVENTARIO FINAL: {inventario_final} unidades")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a22()