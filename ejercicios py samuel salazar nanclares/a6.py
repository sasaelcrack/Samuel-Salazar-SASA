#6. Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.
def a6():
        try:
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_unitario = float(input("Ingrese el precio unitario: $"))
            cantidad = int(input("Ingrese la cantidad comprada: "))

            total = precio_unitario * cantidad

            print(f"\n{'Producto:':<20} {nombre_producto}")
            print(f"{'Precio unitario:':<20} ${precio_unitario:,.2f}")
            print(f"{'Cantidad:':<20} {cantidad}")
            print(f"{'TOTAL A PAGAR:':<20} ${total:,.2f}")
        except ValueError:
             print("debes ingresar un numero valido")

if __name__ == "__main__":
      a6()