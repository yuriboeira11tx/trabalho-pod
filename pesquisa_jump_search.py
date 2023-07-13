import csv
import math
import time


class Pessoa:
    def __init__(self, nome, idade, sexo, profissao):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.profissao = profissao


def pesquisa_jump(arr, valor):
    tamanho = len(arr)
    salto = int(math.sqrt(tamanho))
    anterior = 0

    while arr[min(salto, tamanho) - 1].nome < valor:
        anterior = salto
        salto += int(math.sqrt(tamanho))
        if anterior >= tamanho:
            return None

    while arr[anterior].nome < valor:
        anterior += 1
        if anterior == min(salto, tamanho):
            return None

    if arr[anterior].nome == valor:
        return arr[anterior]

    return None


def buscar_dados_csv(arquivo_csv, valor_busca):
    pessoas = []

    with open(arquivo_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for linha in reader:
            pessoa = Pessoa(linha['nome'], int(
                linha['idade']), linha['sexo'], linha['profissao'])
            pessoas.append(pessoa)

    pessoas_ordenadas = sorted(pessoas, key=lambda p: p.nome)
    resultado_busca = pesquisa_jump(pessoas_ordenadas, valor_busca)

    if resultado_busca is not None:
        return resultado_busca
    else:
        return None


arquivo_csv = 'dados.csv'
valor_busca = 'Carlos'

inicio = time.time()
resultado_busca = buscar_dados_csv(arquivo_csv, valor_busca)
fim = time.time()

if resultado_busca is not None:
    print("Dados encontrados:")
    print(f"Nome: {resultado_busca.nome}")
    print(f"Idade: {resultado_busca.idade}")
    print(f"Sexo: {resultado_busca.sexo}")
    print(f"Profissão: {resultado_busca.profissao}")
    tempo_busca = (fim - inicio) * 1000
    print(f"Tempo de busca: {tempo_busca:.2f} milissegundos")

else:
    print(f"Elemento {valor_busca} não encontrado no arquivo CSV")
