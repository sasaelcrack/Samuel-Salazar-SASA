#*7. Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.*
def a7():
        try:
             valor_compra = float(input("Ingrese el valor total de la compra: $"))

             if valor_compra > 200000:
               descuento = valor_compra * 0.10
               valor_final = valor_compra - descuento
               print(f"\n¡Felicidades! Tiene un descuento del 10%")
               print(f"Valor original: ${valor_compra:,.2f}")
               print(f"Descuento: -${descuento:,.2f}")
               print(f"Valor final: ${valor_final:,.2f}")
             else:
                  print(f"\nNo aplica descuento")
                  print(f"Valor a pagar: ${valor_compra:,.2f}")
        except ValueError:
              print("debes ingresar un numero valido")

if __name__ == "__main__":
      a7()