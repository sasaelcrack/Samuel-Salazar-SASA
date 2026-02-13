#18. Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.
def a18():
         try:
             edad = int(input("Ingrese su edad: "))

             if edad < 18:
                clasificacion = "MENOR DE EDAD"
             elif edad < 60:
                 clasificacion = "ADULTO"
             else:
                 clasificacion = "ADULTO MAYOR"

                 print(f"\nEdad: {edad} años")
                 print(f"Clasificación: {clasificacion}") 
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a18()
