import csv
import time


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        if self.tabela[indice] is None:
            self.tabela[indice] = []
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        resultados = []
        if self.tabela[indice] is not None:
            for item in self.tabela[indice]:
                if item[0] == chave:
                    resultados.append(item[1])
        return resultados


def criar_tabela_hash_from_csv(arquivo_csv, tamanho):
    tabela = TabelaHash(tamanho)
    with open(arquivo_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            chave = row['nome']
            valor = {
                'idade': row['idade'],
                'sexo': row['sexo'],
                'profissao': row['profissao']
            }
            tabela.inserir(chave, valor)
    return tabela


arquivo_csv = 'dados.csv'
tamanho_tabela = 108

inicio = time.time()
tabela = criar_tabela_hash_from_csv(arquivo_csv, tamanho_tabela)
fim = time.time()

nome_busca = 'Laura'
inicio_busca = time.time()
resultados = tabela.buscar(nome_busca)
fim_busca = time.time()

if resultados:
    print("PESQUISA ENCONTRADA:")
    for resultado in resultados:
        print(f"Nome: {nome_busca}")
        print(f"Idade: {resultado['idade']}")
        print(f"Sexo: {resultado['sexo']}")
        print(f"Profissão: {resultado['profissao']}\n")
else:
    print(f"Nenhum dado encontrado para o nome: {nome_busca}")

tempo_total = (fim - inicio) * 1000
tempo_busca = (fim_busca - inicio_busca) * 1000

print(f"Tempo total de execução: {tempo_total:.2f} milissegundos")
print(f"Tempo de busca: {tempo_busca:.2f} milissegundos")
