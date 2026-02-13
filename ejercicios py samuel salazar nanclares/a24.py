#24. Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.
def a24():
         try:
             consumo_m3 = float(input("Ingrese el consumo de agua en m³: "))
             valor_por_m3 = float(input("Ingrese el valor por m³: $"))

             total_factura = consumo_m3 * valor_por_m3

             print(f"\n{'DETALLE DE LA FACTURA'}")
             print(f"Consumo: {consumo_m3} m³")
             print(f"Valor por m³: ${valor_por_m3:,.2f}")
             print(f"TOTAL A PAGAR: ${total_factura:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a24()