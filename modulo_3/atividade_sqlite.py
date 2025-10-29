#1 Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
import sqlite3

conecao = sqlite3.connect("escola_v2.db")
cursor = conecao.cursor()

#2 Faça a query para pegar toda a tabela alunos e imprima na tela.
cursor.execute(
    "Select * from Aluno"
)
alunos = cursor.fetchall()
print("ID | Nome | Data Nascimento | Nota1 | Nota2")
for aluno in alunos:
    print(aluno)


#3 Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos e suas médias.
cursor.execute(
    "Select id, nome, nota1, nota2, (nota1 + nota2) / 2 as media From Aluno Order BY media DESC LIMIT 10"
)
top10_alunos = cursor.fetchall()
print("\nMaiores notas")
print("ID | Nome | Nota1 | Nota2 | Média")
for aluno in top10_alunos:
    print(aluno)

#4 Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
cursor.execute("""
    SELECT Aluno.id, Aluno.nome, Aluno.nota1, Aluno.nota2, Turma.id, Turma.nome
    FROM Aluno
    LEFT JOIN Turma ON Aluno.id_turma = Turma.id
""")
alunos_turmas = cursor.fetchall()
print("\nAlunos e suas turmas (LEFT JOIN):")
print("ID | Nome Aluno | Nota1 | Nota2 | ID Turma | Nome Turma")
for linha in alunos_turmas:
    print(linha)

#5 Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
cursor.execute("""
    SELECT Aluno.id, Aluno.nome, Aluno.nota1, Aluno.nota2, Turma.id, Turma.nome
    FROM Aluno
    LEFT JOIN Turma ON Aluno.id_turma = Turma.id
    WHERE Turma.id = 2
""")
alunos_turma2 = cursor.fetchall()
print("\nAlunos da Turma 2:")
print("ID | Nome Aluno | Nota1 | Nota2 | ID Turma | Nome Turma")
for linha in alunos_turma2:
    print(linha)