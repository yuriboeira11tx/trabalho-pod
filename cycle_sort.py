def cycle_sort(arr):
    n = len(arr)
    trocas = 0

    for ciclo_inicio in range(n - 1):
        item = arr[ciclo_inicio]
        print(f"Ciclo Inicial: {ciclo_inicio}", )
        print(f"Item atual: {item}")

        posicao = ciclo_inicio
        for i in range(ciclo_inicio + 1, n):
            if arr[i] < item:
                posicao += 1

        if posicao == ciclo_inicio:
            continue

        while item == arr[posicao]:
            posicao += 1

        print(f"Posição correta: {posicao}")
        print(f"Lista antes da troca: {arr}")
        arr[posicao], item = item, arr[posicao]
        trocas += 1
        print(f"Lista após a troca: {arr}")

        while posicao != ciclo_inicio:
            posicao = ciclo_inicio
            for i in range(ciclo_inicio + 1, n):
                if arr[i] < item:
                    posicao += 1

            while item == arr[posicao]:
                posicao += 1

            print(f"Posição correta: {posicao}")
            print(f"Lista antes da troca: {arr}")
            arr[posicao], item = item, arr[posicao]
            trocas += 1
            print(f"Lista antes da troca: {arr}")
    return trocas

print("---- Cycle Sort ----")
numeros = [4, 2, 6, 1, 3, 5]
print(f"Lista original: {numeros}")

num_trocas = cycle_sort(numeros)
print(f"\nLista ordenada: {numeros}")
print(f"Número de trocas: {num_trocas}")
