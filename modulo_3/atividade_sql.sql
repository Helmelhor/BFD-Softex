--1
SELECT * from aluno;

--2
SELECT nome, nota1 FROM aluno;

--3
SELECT nome, nota2 from Aluno where nota2 > 8;

--4
SELECT nome from Aluno where data_nascimento > '1999/12/31';

--5
Select nome, mensalidade from Curso where mensalidade > 600;

--6
SELECT * from Turma order by ano;

--7
SELECT ano, COUNT(*) AS quantidade_turmas FROM Turma GROUP BY ano;

--8
SELECT id, AVG(nota1) AS media_nota1
FROM Aluno
GROUP BY id_turma;

--9
SELECT ano, COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano
HAVING COUNT(*) > 2;

--10
SELECT nome, mensalidade
FROM curso
ORDER BY mensalidade DESC;