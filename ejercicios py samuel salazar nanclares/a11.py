#11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.
def a11():
         try:
             valor_ventas = float(input("Ingrese el valor total de ventas: $"))

             comision = valor_ventas * 0.05
             total_recibir = comision

             print(f"\nValor de ventas: ${valor_ventas:,.2f}")
             print(f"Comisión (5%): ${comision:,.2f}")
             print(f"TOTAL A RECIBIR: ${total_recibir:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a11()