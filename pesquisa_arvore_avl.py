import csv
import time


class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor):
        self.raiz = self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no_atual, chave, valor):
        if no_atual is None:
            return Node(chave, valor)
        if chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(
                no_atual.esquerda, chave, valor)
        else:
            no_atual.direita = self._inserir_recursivo(
                no_atual.direita, chave, valor)

        no_atual.altura = 1 + \
            max(self._obter_altura(no_atual.esquerda),
                self._obter_altura(no_atual.direita))
        fator_balanceamento = self._calcular_fator_balanceamento(no_atual)

        if fator_balanceamento > 1 and chave < no_atual.esquerda.chave:
            print("Rotação Simples à Direita:")
            return self._rotacao_direita(no_atual)

        if fator_balanceamento < -1 and chave > no_atual.direita.chave:
            print("Rotação Simples à Esquerda:")
            return self._rotacao_esquerda(no_atual)

        if fator_balanceamento > 1 and chave > no_atual.esquerda.chave:
            print("Rotação Dupla à Direita:")
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if fator_balanceamento < -1 and chave < no_atual.direita.chave:
            print("Rotação Dupla à Esquerda:")
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no_atual, chave):
        if no_atual is None or no_atual.chave == chave:
            return no_atual.valor
        if chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerda, chave)
        else:
            return self._buscar_recursivo(no_atual.direita, chave)

    def _obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _calcular_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._obter_altura(z.esquerda),
                           self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda),
                           self._obter_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._obter_altura(z.esquerda),
                           self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda),
                           self._obter_altura(y.direita))

        return y


def criar_arvore_avl_from_csv(arquivo_csv):
    arvore = ArvoreAVL()
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
arvore = criar_arvore_avl_from_csv(arquivo_csv)
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
