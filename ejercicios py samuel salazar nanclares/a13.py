#13. Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).
def a13():
         try:
             nota1 = float(input("Ingrese la primera nota: "))
             nota2 = float(input("Ingrese la segunda nota: "))
             nota3 = float(input("Ingrese la tercera nota: "))

             promedio = (nota1 + nota2 + nota3) / 3

             if promedio >= 3.0:
                resultado = "APROBADO"
             else:
                 resultado = "REPROBADO"

                 print(f"\nNota 1: {nota1}")
                 print(f"Nota 2: {nota2}")
                 print(f"Nota 3: {nota3}")
                 print(f"Promedio: {promedio:.2f}")
                 print(f"Estado: {resultado}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a13()