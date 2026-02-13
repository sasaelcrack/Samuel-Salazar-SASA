#20. Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.
def a20():
         try:
             capital = float(input("Ingrese el capital inicial: $"))
             tasa_interes = float(input("Ingrese la tasa de interés mensual (%): "))
             tiempo_meses = int(input("Ingrese el tiempo en meses: "))

             interes = capital * (tasa_interes / 100) * tiempo_meses 
             total = capital + interes

             print(f"\nCapital inicial: ${capital:,.2f}")
             print(f"Tasa de interés: {tasa_interes}% mensual")
             print(f"Tiempo: {tiempo_meses} meses")
             print(f"Interés generado: ${interes:,.2f}")
             print(f"TOTAL A PAGAR: ${total:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a20()

        