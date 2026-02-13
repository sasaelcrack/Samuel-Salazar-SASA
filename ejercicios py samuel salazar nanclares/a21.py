#21. Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.
def a21():
         try:
             capital = float(input("Ingrese el capital inicial: $"))
             tasa_interes = float(input("Ingrese la tasa de interés por período (%): "))
             periodos = int(input("Ingrese el número de períodos: "))

             monto_final = capital * ((1 + tasa_interes / 100) ** periodos)
             interes_generado = monto_final - capital

             print(f"\nCapital inicial: ${capital:,.2f}")
             print(f"Tasa de interés: {tasa_interes}% por período")
             print(f"Número de períodos: {periodos}")
             print(f"Interés generado: ${interes_generado:,.2f}")
             print(f"MONTO FINAL: ${monto_final:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a21()