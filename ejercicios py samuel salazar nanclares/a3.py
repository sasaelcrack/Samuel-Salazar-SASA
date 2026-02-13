#3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
def a3():
          try:
              celsius = float(input("Ingrese la temperatura en grados Celsius: "))

              fahrenheit = (celsius * 9/5) + 32

              print(f"\n{celsius}°C = {fahrenheit}°F")

          except ValueError:
           print("debes ingresar un numero valido")

if __name__ == "__main__":
      a3()
