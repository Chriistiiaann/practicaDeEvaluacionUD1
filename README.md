# Práctica Unidad 1 - Puesta En Producción Segura (PPS)

Este repositorio contiene la resolución de la **Práctica de Evaluación de la Unidad 1**, desarrollada como parte de la asignatura **Puesta en Producción Segura (PPS)** del Curso de Especialización en Ciberseguridad.

El proyecto implementa una aplicación modular en Python que combina lógica matemática, validación de datos y una suite completa de pruebas unitarias utilizando dos frameworks distintos.

## 📋 Características

### Lógica

* **Conversor Binario (`binario.py`):** Algoritmo capaz de validar y convertir cadenas binarias a su valor decimal equivalente.

* **Validación de Listas y Rangos (`lista.py`):** Funciones reutilizables para comprobar si un número pertenece a un rango específico (1-20) y si existe dentro de una lista de control predefinida.

### Interfaz de Usuario (`main.py`)

* **CLI Interactiva:** Menú de consola robusto con gestión de errores.

* **Historial de Operaciones:** Registro en memoria de las conversiones y comprobaciones realizadas durante la sesión.

* **Experiencia de Usuario:** Limpieza automática de pantalla compatible con Windows (`cls`) y Linux/Mac (`clear`).

### Testing (QA)

* **Unittest:** Suite de pruebas estándar con recorrido iterativo de casos (`subtests`).

* **Pytest:** Implementación moderna utilizando decoradores (`@parametrize`) y accesorios de datos (`@fixtures`).

## 🚀 Instalación y Uso

### Prerrequisitos

* Python 3.11 o superior.

* Librería `pytest` (para ejecutar las pruebas del ejercicio 5).

### 1. Clonar el repositorio

```bash
git clone [https://github.com/Chriistiiaann/practicaDeEvaluacionUD1.git](https://github.com/Chriistiiaann/practicaDeEvaluacionUD1.git)
cd practicaDeEvaluacionUD1
```

### 2. Ejecutar el programa principal
```bash
py src/main.py
```
### 3. Ejecución de los test
- Opción A: Test con Unittest
```bash
py -m unittest discover -s src/tests -t src -v
```
- Opción B: Test con Pytest
```bash
py -m pytest src/tests/testPyTests.py -v
```

## 📂 Estructura del Proyecto
```bash 
practicaDeEvaluacionUD1/
├── src/
│   ├── ejercicio2/
│   │   ├── __init__.py
│   │   └── binario.py          # Lógica Ejercicio 2
│   ├── ejercicio3/
│   │   ├── __init__.py
│   │   └── lista.py            # Lógica Ejercicio 3
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── testUnitTest.py     # Tests Ejercicio 4 (Unittest)
│   │   └── testPyTests.py      # Tests Ejercicio 5 (Pytest)
│   └── main.py                 # Punto de entrada (Menú Principal)
├── .gitignore
└── README.md                   # Documentación del proyecto
```

## 🛠️ Tecnologías Utilizadas
- Lenguaje: Python 3
- Gestión de Entorno: Módulos os y sys.
- Frameworks de Pruebas:
    - unittest 
    - pytest 

## ✒️ Autor
Christian Rodríguez Lara

Asignatura: Puesta en Producción Segura (PPS)

Última modificación: 30/11/2025