#4. Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.
def a4():
        try:
              horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
              valor_hora = float(input("Ingrese el valor por hora: $"))

              salario = horas_trabajadas * valor_hora 

              print(f"\nSalario semanal: ${salario:,.2f}")

        except ValueError:
             print("debes ingresar un numero valido")

if __name__ == "__main__":
      a4()
