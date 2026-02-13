#Venta diaria de un almacén: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta
def a25():
         try:
             numero_ventas = int(input("Ingrese el número de ventas realizadas: "))

             total_vendido = 0

             for i in range(1, numero_ventas + 1):
              valor_venta = float(input(f"Ingrese el valor de la venta {i}: $"))
             total_vendido += valor_venta

             if numero_ventas > 0:
               promedio_venta = total_vendido / numero_ventas
             else:
                promedio_venta = 0

                print(f"\n{'RESUMEN DEL DÍA'}")
                print(f"Número de ventas: {numero_ventas}")
                print(f"Total vendido: ${total_vendido:,.2f}")
                print(f"Promedio por venta: ${promedio_venta:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a25()
