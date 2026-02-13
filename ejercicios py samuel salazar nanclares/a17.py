#17. Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.
def a17():
         try:
             año_nacimiento = int(input("Ingrese su año de nacimiento: "))
             año_actual = int(input("Ingrese el año actual: "))

             edad = año_actual - año_nacimiento

             print(f"\nUsted tiene {edad} años")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a17()
