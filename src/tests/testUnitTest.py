import unittest

from ejercicio2.binario import esBinario
from ejercicio3.lista import estaEnRango, estaEnLista

"""
tests/testUniTest.py
Suite de pruebas unitarias basada en unittest para validar las funciones
de los ejercicios 2 y 3. Completando el ejercicio 4.

Ultima Modificación: 30/11/2025
Autor: Christian Rodríguez Lara
Dependencias: unittest, ejercicio2.binario, ejercicio3.lista
"""

class TestFuncionesEjercicios(unittest.TestCase):

    def testEsBinario(self):
        """
        Prueba parametrizada para validar la función esBinario (Ejercicio 2).
        Comprueba cadenas válidas, inválidas, vacías y tipos mixtos.
        """
        casos = [
            #Casos Válidos
            ("1", True),
            ("0", True),
            ("101010", True),
            ("111111", True),
            ("000000", True), 

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
            #CHRISTIAN RODRÍGUEZ LARA
        ]

        for entrada, esperado in casos: #Christian Rodríguez Lara
            with self.subTest(entrada=entrada):
                resultadoReal = esBinario(entrada)
                self.assertEqual(resultadoReal, esperado, msg=f"Fallo en esBinario con entrada: '{entrada}'")

    def testEstaEnRango(self):
        """
        Prueba parametrizada para validar estaEnRango (Ejercicio 3).
        Verifica límites inclusivos y valores fuera de rango.
        Estructura de caso: (valor, minimo, maximo, esperado)
        """
        casos = [
            # Dentro del Rango
            (6, 1, 20, True),   
            (1, 1, 20, True),   
            (20, 1, 20, True), 
                                #christian rodríguez lara
            # Fuera del Rango
            (0, 1, 20, False), 
            (21, 1, 20, False), 
            (-5, 1, 20, False), 
            (100, 1, 20, False) 
        ]

        for valor, minimo, maximo, esperado in casos: #Christian Rodríguez Lara
            with self.subTest(valor=valor, rango=f"[{minimo}-{maximo}]"):
                resultadoReal = estaEnRango(valor, minimo, maximo)
                self.assertEqual(resultadoReal, esperado, msg=f"Fallo en estaEnRango: {valor} en [{minimo}, {maximo}]")

    def testEstaEnLista(self):
        """
        Prueba parametrizada para validar estaEnLista (Ejercicio 3).
        Verifica pertenencia de elementos en listas numéricas.
        Estructura de caso: (valor, lista, esperado)
        """
        listaPrueba = [6, 14, 11, 3, 2, 1, 15, 19]
        listaVacia = []

        casos = [
            # En la Lista
            (6, listaPrueba, True),    
            (19, listaPrueba, True),   
            (3, listaPrueba, True),    
                                    #Christian Rodríguez Lara
            # No en la Lista
            (20, listaPrueba, False),  
            (0, listaPrueba, False),   
            (7, listaPrueba, False),   
            (-1, listaPrueba, False),  
            (1, listaVacia, False)     
        ]

        for valor, lista, esperado in casos: #Chrisian Rodríguez Lara
            with self.subTest(valor=valor, lista=lista):
                resultadoReal = estaEnLista(valor, lista)
                self.assertEqual(resultadoReal, esperado, msg=f"Fallo en estaEnLista buscando {valor} en {lista}")

if __name__ == '__main__' : unittest.main()