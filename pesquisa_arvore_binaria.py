import csv
import time

class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor):
        novo_no = Node(chave, valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, no_atual, novo_no):
        if novo_no.chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._inserir_recursivo(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._inserir_recursivo(no_atual.direita, novo_no)

    def buscar(self, chave):
        return self.buscar_recursivo(self.raiz, chave)

    def buscar_recursivo(self, no_atual, chave):
        if no_atual is None:
            return None
        if no_atual.chave == chave:
            return no_atual.valor
        if chave < no_atual.chave:
            return self.buscar_recursivo(no_atual.esquerda, chave)
        else:
            return self.buscar_recursivo(no_atual.direita, chave)

def criar_arvore_binaria_from_csv(arquivo_csv):
    arvore = ArvoreBinariaBusca()
    with open(arquivo_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            chave = row['nome']
            valor = {
                'idade': row['idade'],
                'sexo': row['sexo'],
                'profissao': row['profissao']
            }
            arvore.inserir(chave, valor)
    return arvore

arquivo_csv = 'dados.csv'

inicio = time.time()
arvore = criar_arvore_binaria_from_csv(arquivo_csv)
fim = time.time()

nome_busca = 'Carlos'
inicio_busca = time.time()
resultado = arvore.buscar(nome_busca)
fim_busca = time.time()

if resultado is not None:
    print("Dados encontrados:")
    print(f"Nome: {nome_busca}")
    print(f"Idade: {resultado['idade']}")
    print(f"Sexo: {resultado['sexo']}")
    print(f"Profissão: {resultado['profissao']}")
else:
    print(f"Nenhum dado encontrado para o nome: {nome_busca}")

tempo_total = (fim - inicio) * 1000 
tempo_busca = (fim_busca - inicio_busca) * 1000

print(f"Tempo total de execução: {tempo_total:.2f} milissegundos")
print(f"Tempo de busca: {tempo_busca:.2f} milissegundos")
