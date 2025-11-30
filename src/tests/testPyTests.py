import pytest
from ejercicio2.binario import esBinario
from ejercicio3.lista import estaEnRango, estaEnLista

"""
src/tests/ejercicio5/test_pytest.py
Suite de pruebas unitarias implementada con Pytest (Ejercicio 5).
Replica la lógica de validación del Ejercicio 4 pero usando decorators.

Ultima Modificación: 30/11/2025
Autor: Christian Rodríguez Lara
Dependencias: pytest, ejercicio2.binario, ejercicio3.lista
"""

@pytest.mark.parametrize("entrada, esperado", [
    #Casos Válidos
    ("1", True),
    ("0", True),
    ("101010", True),
    ("111111", True), 
    ("000000", True),  #Christian Rodríguez Lara
    
    # Casos NO Válidos
    ("6", False),           
    ("10012", False),      
    ("abcd", False),        
    ("10abc1", False),      
    ("-1001", False),        
    (" 1001", False),       
    ("1011 ", False),        
    ("", False),            
    ("10.110", False)      
])
def testEsBinario(entrada, esperado):
    """
    Verifica que la función esBinario identifique correctamente 
    cadenas válidas e inválidas.
    """
    if entrada is None:
        pass     
    assert esBinario(entrada) == esperado, f"Falló con la entrada: '{entrada}'"

@pytest.mark.parametrize("valor, minimo, maximo, esperado", [
    # Dentro del Rango
    (6, 1, 20, True),   
    (1, 1, 20, True),   
    (20, 1, 20, True),  #Christian Rodríguez Lara

    # Fuera del Rango
    (0, 1, 20, False),  
    (21, 1, 20, False), 
    (-5, 1, 20, False), 
    (100, 1, 20, False) 
])
def testEstaEnRango(valor, minimo, maximo, esperado):
    """
    Verifica que estaEnRango respete los límites inclusivos.
    """
    assert estaEnRango(valor, minimo, maximo) == esperado

@pytest.fixture
def listaPrueba():
    return [6, 14, 11, 3, 2, 1, 15, 19]

@pytest.mark.parametrize("valor, esperado", [
    # Está en la lista
    (6, True),      
    (19, True),     
    (3, True),      #Christian Rodríguez Lara
    (1, True),

    # No está en la lista
    (20, False),    
    (0, False),     
    (7, False),     
    (-1, False)     
])
def testEstaEnLista(listaPrueba, valor, esperado):
    """
    Verifica si un elemento pertenece a la lista dada.
    Recibe 'listaPrueba' automáticamente gracias al nombre del argumento.
    """
    assert estaEnLista(valor, listaPrueba) == esperado