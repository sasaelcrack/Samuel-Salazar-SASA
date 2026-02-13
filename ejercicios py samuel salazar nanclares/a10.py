#10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.
def a10():
         try:
             cantidad_productos = int(input("¿Cuántos productos va a comprar?: "))

             total_compra = 0

             for i in range(1, cantidad_productos + 1):
              precio = float(input(f"Ingrese el precio del producto {i}: $"))
              total_compra += precio

              print(f"Total de productos: {cantidad_productos}")
              print(f"TOTAL DE LA COMPRA: ${total_compra:,.2f}")
         except ValueError:
                  print("debes ingresar un numero valido")

if __name__ == "__main__":
      a10()