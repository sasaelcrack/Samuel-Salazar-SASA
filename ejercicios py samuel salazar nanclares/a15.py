#15. Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.
def a15():
         try:
             numero1 = int(input("Ingrese el primer número: "))
             numero2 = int(input("Ingrese el segundo número: "))

             print()
             if numero1 > numero2:
              print(f"El número mayor es: {numero1}")
             elif numero2 > numero1:
              print(f"El número mayor es: {numero2}")
             else:
              print(f"Los números son iguales: {numero1}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a15()
