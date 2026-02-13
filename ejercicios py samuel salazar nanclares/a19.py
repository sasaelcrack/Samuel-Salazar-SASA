#19. Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.
def a19():
         try:
             pesos = float(input("Ingrese el valor en pesos colombianos: $"))
             tasa_cambio = float(input("Ingrese la tasa de cambio (pesos por dólar): "))

             dolares = pesos / tasa_cambio

             print(f"\n{pesos:,.2f} pesos colombianos = ${dolares:,.2f} USD")
             print(f"Tasa de cambio: {tasa_cambio:,.2f} COP/USD")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a19()

        