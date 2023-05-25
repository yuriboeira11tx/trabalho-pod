def odd_even_sort(numeros):
    ordenado = False
    tamanho = len(numeros)
    
    while not ordenado:
        ordenado = True

        # Fase impar
        for i in range(1, tamanho-1, 2):
            if numeros[i] > numeros[i+1]:
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
                ordenado = False
                print(f"Fase impar: {numeros}")
        
        # Fase par
        for i in range(0, tamanho-1, 2):
            if numeros[i] > numeros[i+1]:
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
                ordenado = False
                print(f"Fase par: {numeros}")
    return numeros

print("---- Odd-Even Sort ----")
numeros = [3, 2, 3, 8, 5, 6, 4, 1]
print(f"Lista original: {numeros}")

numeros_ordenados = odd_even_sort(numeros)
print(f"Lista ordenada: {numeros_ordenados}")
