# En este commit hemos realizado un programa de Ordenación de Arreglo Multidimensional
# Autor: Juan Pablo Ramirez Benitez | Primer Nivel "F"

def bubble_sort(fila):
    """
    Implementa Bubble Sort para ordenar una fila de la matriz en orden ascendente.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores

# Definir la matriz 3x3
matriz = [
    [4, 7, 1],
    [9, 2, 8],
    [5, 3, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_ordenar = int(input("\nIngrese el número de fila (0-2) que desea ordenar: "))

# Validar que la fila ingresada sea válida
if 0 <= fila_a_ordenar < len(matriz):
    bubble_sort(matriz[fila_a_ordenar])  # Ordenar la fila elegida
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("\nNúmero de fila inválido. Debe estar entre 0 y 2.")


