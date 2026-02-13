#9. Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.
def a9():
        try:
             valor_sin_iva = float(input("Ingrese el valor de la venta sin impuestos: $"))

             iva = valor_sin_iva * 0.19
             total_con_iva = valor_sin_iva + iva

             print(f"\nValor sin IVA: ${valor_sin_iva:,.2f}")
             print(f"IVA (19%): ${iva:,.2f}")
             print(f"TOTAL CON IVA: ${total_con_iva:,.2f}")
        except ValueError:
              print("debes ingresar un numero valido")

if __name__ == "__main__":
      a9()