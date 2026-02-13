#16. Número par o impar: Solicitar un número entero e indicar si es par o impar.
def a16():
         try:
             numero = int(input("Ingrese un número entero: "))

             if numero % 2 == 0:
                resultado = "PAR"
             else:
                 resultado = "IMPAR"

                 print(f"\nEl número {numero} es {resultado}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a16()
