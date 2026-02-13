#2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
def a2():
        try:
             base = float(input("Ingrese la base del rectángulo: "))
             altura = float(input("Ingrese la altura del rectángulo: "))

             area = base * altura

             print(f"\nEl área del rectángulo es: {area}")
            
        except ValueError:
           print("debes ingresar un numero valido")

if __name__ == "__main__":
      a2()
