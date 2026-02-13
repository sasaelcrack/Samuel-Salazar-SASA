#23. Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.
def a23():
         try:
             peso = float(input("Ingrese el peso del paquete en kg: "))

             if peso <= 5:
                 costo_envio = 10000
             else:
                 costo_envio = 20000

                 print(f"\nPeso del paquete: {peso} kg")
                 print(f"Costo de envío: ${costo_envio:,.2f}")
         except ValueError:
                   print("debes ingresar un numero valido")

if __name__ == "__main__":
      a23()