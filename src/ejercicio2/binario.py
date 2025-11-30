"""
 src/ejercicio2/binario.py
 Ejercicio 2: Validación de cadenas binarias.
 Ultima Modificación: 30/11/2025
 Autor: Christian Rodríguez Lara
"""
def esBinario(numeroBinario):
    """
    Devuelve True o False si la cadena de caracteres (numeroBinario) que se ha pasado
    como parámetro contiene una cadena binaria.
    """
    if not numeroBinario:
        return False
        
    for caracter in numeroBinario:
        if caracter not in ('0', '1'):
            return False
    return True
