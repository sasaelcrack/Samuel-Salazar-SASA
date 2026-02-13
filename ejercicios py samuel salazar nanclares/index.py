#index:Py
#creado por samuel salazar


import os #interactua con el sistema operativo 
#(archivos, directivos,rutas,variables de entorno).

import sys #maneja la configuracion y el entorno del interprete de phyton
#(argumentos de linea de comandos, rutas de modulos )

import subprocess #ejecuta comando externos y programas controlando sus 
#entradas/salidas y errores

while True:
    print("========================================")
    print("taller 1 - algoritmos basicos en phyton")
    print("By samuel Salazar Nanclares")
    print("Menu Principal")
    print("========================================")
    
    for i in range (1, 26):
        print(f"ejecutar algoritmo{i}")
    print("0.Salir\n")

    opcion = input("seleccione una opcion: ")

    if opcion =="0":
        print("Saliendo ...")
        break

    if opcion.isdigit() and 1 <= int(opcion) <=25:
        archivo = f"a{opcion}.py"

        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"no existe {archivo}")
    
    else:    
        print("Opcion no valida")



    
    input("\n Presiona ENTER para continuar")