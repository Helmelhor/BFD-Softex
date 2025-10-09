# 1. Associação: Pessoa e Livro
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo


pessoa = Pessoa("Ana")
livro = Livro("Python Básico")
print(f"{pessoa.nome} está lendo o livro '{livro.titulo}'")

# 2. Associação: Aluno e Ônibus
class Onibus:
    def __init__(self, linha):
        self.linha = linha

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def pegar_onibus(self, onibus):
        print(f"{self.nome} pegou o ônibus da linha {onibus.linha}")

onibus1 = Onibus(123)
aluno1 = Aluno("Carlos")
aluno1.pegar_onibus(onibus1)

# 3. Agregação: Funcionario e Departamento
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

f1 = Funcionario("João")
f2 = Funcionario("Maria")
dep = Departamento("RH")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)
print(f"Departamento {dep.nome} possui: {[f.nome for f in dep.funcionarios]}")

# 4. Agregação: Time e Jogador
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

j1 = Jogador("Pedro", "Atacante")
j2 = Jogador("Lucas", "Goleiro")
time = Time("Tigres")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
print(f"Time {time.nome} tem jogadores: {[j.nome for j in time.jogadores]}")

# 5. Composição: Carro e Motor
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

carro = Carro("Fusca", 1300)
print(f"Carro: {carro.modelo}, Motor: {carro.motor.potencia}cc")
del carro  
# print(carro.motor)  # Isso daria erro, pois carro não existe mais

# 6. Composição: Casa e Comodos
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [Comodo("Sala"), Comodo("Cozinha"), Comodo("Quarto"), Comodo("Banheiro")]

casa = Casa()
print(f"A casa possui os cômodos: {[c.nome for c in casa.comodos]}")
