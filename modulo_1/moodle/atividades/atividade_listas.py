# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["harry potter", "senhor dos aneis", "1984"]
# 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
print(livros[0])
print(livros[-1])
# 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("Duna")
livros.append("O Hobbit")
print(livros)
# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(2, "Duna")
print(livros)
# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if "Silêncio dos inocentes" not in livros:
    print("Livro não encontrado")
else:
    livros.remove("Silêncio do inocentes")
# 6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

cont = 0
numeros = [1, 2, 3, 2, 4, 2, 5]

for numero in numeros:
    if numero == 2:
        cont += 1

print(cont)

# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for livro in livros:
    print(f"O livro {livro} é interessante")

# 8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12,18,25,14,30]

for idade in idades:
    if idade >= 18:
        print(idade)

# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma = 0
for valor in valores:
    soma += valor
print(soma)

# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
import statistics
cont = 1
notas = []
notas1 = []
notas2 = []
media1 = 0
media2 = 0

while cont <= 1:
    aluno1_resultado1 = int(input(f"Digite sua nota: "))
    aluno1_resultado2 = int(input(f"Digite sua nota: "))
    aluno1_resultado3 = int(input(f"Digite sua nota: "))
    notas1.append(aluno1_resultado1)
    notas1.append(aluno1_resultado2)
    notas1.append(aluno1_resultado3)
    cont+=1

while cont <= 2:
    aluno2_resultado1 = int(input(f"Digite sua nota: "))
    aluno2_resultado2 = int(input(f"Digite sua nota: "))
    aluno2_resultado3 = int(input(f"Digite sua nota: "))
    notas2.append(aluno2_resultado1)
    notas2.append(aluno2_resultado2)
    notas2.append(aluno2_resultado3)
    cont+=1

notas += notas1
notas += notas2
print(notas)
statistics.mean(notas1)
statistics.mean(notas2)


# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
# [ ] - para posições vazias
# tor - para a torre
# cav - para o cavalo
# bis - para o bispo
# rai - para a rainha
# rei - para o rei
# pea - para o peão
