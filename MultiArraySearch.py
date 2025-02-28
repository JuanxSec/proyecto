# En este commit hemos realizado un programa de Búsqueda en Arreglo Multidimensional
# Autor: Juan Pablo Ramirez Benitez | Primer Nivel "F"

def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz 3x3 y devuelve su posición.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Devuelve la posición si se encuentra el valor
    return None  # Devuelve None si el valor no está en la matriz

# Definir la matriz 3x3
matriz = [
    [4, 7, 1],
    [9, 2, 8],
    [5, 3, 6]
]

# Mostrar la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Solicitar al usuario un número para buscar
valor_a_buscar = int(input("\nIngrese el valor que desea buscar en la matriz: "))

# Realizar la búsqueda
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostrar resultados
if resultado:
    print(f"\nEl valor {valor_a_buscar} se encuentra en la posición: {resultado}")
else:
    print(f"\nEl valor {valor_a_buscar} no está en la matriz.")
