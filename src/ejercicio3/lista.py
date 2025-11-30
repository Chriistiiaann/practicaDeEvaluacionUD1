"""
 src/ejercicio3/lista.py
Ejercicio 3: Comprobación de rangos y listas.
Basado en el ejercicio de la pág. 35 del libro 'Introducción a Python'.
Ultima Modificación: 30/11/2025
Autor: Christian Rodríguez Lara
"""

def estaEnRango(valor, minimo, maximo):
    """
    Devuelve True o False determinando si el valor se encuentra 
    entre el mínimo y el máximo (ambos incluidos).
    CHRISTIAN RODRÍGUEZ LARA
    """
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    """
    Devuelve True o False determinando si el valor está en la lista.
    CHRISTIAN RODRÍGUEZ LARA
    """
    return valor in lista