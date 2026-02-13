#8. Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.
def a8():
        try:
             precio = float(input("Ingrese el precio del producto: $"))
             porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

             valor_descuento = precio * (porcentaje_descuento / 100)
             precio_final = precio - valor_descuento

             print(f"\nPrecio original: ${precio:,.2f}")
             print(f"Descuento ({porcentaje_descuento}%): -${valor_descuento:,.2f}")
             print(f"Precio final: ${precio_final:,.2f}")
        except ValueError:
              print("debes ingresar un numero valido")

if __name__ == "__main__":
      a8()
