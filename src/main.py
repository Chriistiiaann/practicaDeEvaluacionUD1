"""
main.py
Programa principal que implementa la interfaz de usuario (CLI) para
la Puesta en Producción Segura (Unidad 1).
Gestiona el menú de navegación, centrado en el Ejercicio 2 y 3.
Ultima Modificación. 30/11/2025
Autor. Christian Rodríguez Lara
Dependencias. os, src.ejercicio2.binario, src.ejercicio3.lista
"""
import os
from ejercicio2.binario import esBinario
from ejercicio3.lista import estaEnLista, estaEnRango


def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    if os.name == 'nt':
        os.system('cls') # Christian Rodríguez Lara
    else:
        os.system('clear')  

def main():
    historialBinario = []
    historialLista = []
    listaEjercicio3 = [6, 14, 11, 3, 2, 1, 15, 19]
    while True:
        limpiar_pantalla()

        print("===============================================")
        print("   Práctica Unidad 1 - Puesta En Producción    ")
        print("           Christian Rodríguez Lara            ")
        print("===============================================")
        print("\n1. Ejercicio 2: Conversor Binario a Decimal")
        print("2. Ejercicio 3: Comprobación en Lista (1-20)")
        print("3. Ver historial de conversiones de binario a decimal")
        print("4. Ver historial de comprobaciones en lista")
        print("5. Salir del programa")

        opcion = input("\nSelecciona una opción (1-5): ")

        match opcion:
            case '1':
                limpiar_pantalla() 
                print("====================================================================")
                print("      Ejercicio 2: Binario a Decimal - Christian Rodríguez Lara     ")
                print("====================================================================\n")
                while True: 
                    dato = input("Introduce un número binario (o 'volver'): ")
                    
                    if not dato.strip():
                        print("No se ha introducido ningún dato. Por favor introduzca un número binario o 'volver'.\n")
                        continue
                    
                    if dato.lower() == 'volver':
                        break
                    
                    if esBinario(dato):
                        # Convertimos de base 2 a entero
                        decimal = int(dato, 2)
                        resultado = f"Binario '{dato}' es {decimal} en decimal."
                        print(f"{resultado}\n")
                        historialBinario.append(resultado)
                    else:
                        print("El dato introducido NO es un binario válido. Por favor introduce un número binario correcto.\n")
            case '2':
                limpiar_pantalla()
                print("====================================================================")
                print("      Ejercicio 3: Comprobación Lista - Christian Rodríguez Lara    ")
                print("====================================================================")
                print(f"Lista de referencia: {listaEjercicio3}")
                print("El número debe estar entre 1 y 20.\n")

                while True:
                    dato = input("Introduce un número del 1 al 20 (o 'volver'): ")

                    if not dato.strip():
                        print("No se ha introducido ningún dato. Por favor introduzca un número del 1 al 20 o 'volver'.\n")
                        continue

                    if dato.lower() == 'volver':
                        break

                    
                    if dato.isdigit(): # Validamos si es numérico antes de convertir
                        numero = int(dato)
                                               
                        if estaEnRango(numero, 1, 20): #Comprobación sobre si está en rango
                            
                            enLista = estaEnLista(numero, listaEjercicio3) #Comprobación sobre si está en la lista
                            
                            if enLista:
                                msg = f"El número {numero} ESTÁ en la lista."
                            else:
                                msg = f"El número {numero} NO está en la lista (aunque está en rango)."
                            
                            resultado = f"{msg}"
                            print(f"{msg}\n")
                            historialLista.append(resultado)
                        
                        else:
                            print("El número debe estar entre 1 y 20.\n")

                    else:
                        print("Debes introducir un valor numérico entero.\n")
            case '3':
                limpiar_pantalla() 
                print("=================================================================")
                print("      Historial de Operaciones - Christian Rodríguez Lara        ")
                print("=================================================================\n")
                if len(historialBinario) == 0: 
                    print("\nEl historial está vacío.")
                else:
                    for i, h in enumerate(historialBinario, 1):
                        print(f"{i}. {h}")
                
                input("\nPresiona ENTER para volver al menú...")     
            
            case '4':
                limpiar_pantalla() 
                print("=================================================================")
                print("     Historial de Números en Lista - Christian Rodríguez Lara    ")
                print("=================================================================\n")
                if len(historialLista) == 0: 
                    print("\nEl historial está vacío.")
                else:
                    for i, h in enumerate(historialLista, 1):
                        print(f"{i}. {h}")
                
                input("\nPresiona ENTER para volver al menú...")

            case '5': #Christian Rodríguez Lara
                print("\n¡Gracias por usar el programa!")
                break
            
            case _:
                print("\nOpción no válida, elige entre 1 y 5.")
                input("\nPresiona ENTER para intentar de nuevo...")

if __name__ == "__main__" : main()