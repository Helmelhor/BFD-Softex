# 1. Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
aluno = {"nome": "João", "idade": 20, "nota": 8.5}

# 2. Dado o dicionário:
# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# Imprima o nome do produto e a quantidade em estoque.
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print(produto["nome"])
print(produto["estoque"])

# 3. Dado o dicionário:
# pessoa = {"nome": "Carlos", "idade": 30}
# Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"

# 4. Dado o dicionário:
# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# Remova a chave "ano" do dicionário.
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"]
print(carro)

# 5. Verifique se a chave "telefone" existe no dicionário:
# contato = {"nome": "Ana", "email": "ana@email.com"}
contato = {"nome": "Ana", "email": "ana@email.com"}
if "telefone" in contato:
    print("telefone existe no dicionário")
else:
    print("não existe")

# 6. Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def conta_palavra(lista):
    cont = {}
    for palavra in lista:
        if palavra in cont:
            cont[palavra] += 1
        else:
            cont[palavra] = 1
    return cont

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(conta_palavra(palavras))

# 7. Dado o dicionário:
# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d = {"a": 1, "b": 2, "c": 3}

d_invertido = {valor: chave for chave, valor in d.items()}

# 8. Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

alunos = {
    "João": [7.5, 8.0, 9.0],
    "Maria": [9.5, 8.5, 10.0],
    "Pedro": [6.0, 7.0, 8.0]
}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"Média de {aluno}: {media}")

# 9. Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.

def mescla_dicionarios(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

# 10. Dado o dicionário:
# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
for aluno, pontuacao in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
    print(f"{aluno}: {pontuacao}")