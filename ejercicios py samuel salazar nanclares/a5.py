#5. Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.
def a5():
        try:
             horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
             valor_hora = float(input("Ingrese el valor por hora: $"))

             if horas_trabajadas <= 40:
              salario = horas_trabajadas * valor_hora
             else:
              horas_normales = 40
             horas_extra = horas_trabajadas - 40
             salario = (horas_normales * valor_hora) + (horas_extra * valor_hora * 1.5)

             print(f"\nHoras trabajadas: {horas_trabajadas}")
             if horas_trabajadas > 40:
              print(f"Horas normales: 40")
             print(f"Horas extra: {horas_trabajadas - 40}")
             print(f"Salario total: ${salario:,.2f}")
        except ValueError:
             print("debes ingresar un numero valido")

