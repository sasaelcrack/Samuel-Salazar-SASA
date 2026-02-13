#14. Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.
def a14():
         try:
             nota_talleres = float(input("Ingrese la nota de talleres: "))
             nota_parcial = float(input("Ingrese la nota del examen parcial: "))
             nota_final = float(input("Ingrese la nota del examen final: "))

             nota_definitiva = (nota_talleres * 0.30) + (nota_parcial * 0.30) + (nota_final * 0.40)

             print(f"\n{'Actividad':<20} {'Nota':<10} {'Ponderación':<15} {'Contribución'}")
             print(f"{'Talleres':<20} {nota_talleres:<10.2f} {'30%':<15} {nota_talleres * 0.30:.2f}")
             print(f"{'Examen parcial':<20} {nota_parcial:<10.2f} {'30%':<15} {nota_parcial * 0.30:.2f}")
             print(f"{'Examen final':<20} {nota_final:<10.2f} {'40%':<15} {nota_final * 0.40:.2f}")
             print(f"NOTA DEFINITIVA: {nota_definitiva:.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a14()