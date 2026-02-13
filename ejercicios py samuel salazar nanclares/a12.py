#11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.
def a12():
         try:
              ventas_mensuales = float(input("Ingrese el valor de ventas mensuales: $"))

              if ventas_mensuales > 1000000:
                porcentaje = 10
                comision = ventas_mensuales * 0.10
              else:
                  porcentaje = 5
                  comision = ventas_mensuales * 0.05

                  print(f"\nVentas mensuales: ${ventas_mensuales:,.2f}")
                  print(f"Porcentaje de comisión: {porcentaje}%")
                  print(f"Comisión a recibir: ${comision:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a12()
