# 1. Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
class pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Oi meu nome é {self.nome}, tenho {self.idade} anos")

helmer = pessoa("helmer", 19)



# 2. Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

helmer.apresentar()


# 3. Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = carro("Fiat","Uno", "1999")
carro2 = carro("Toyota","Corolla", "2011")
carro3 = carro("Honda", "Civic LSX", "2016")
        

# 4. Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
carro4 = carro("Jeep","Renegade","2025")
print(carro4.ano)

carro4.ano = "2001"
print(carro4.ano)

# 5. Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
    def sacar(self,valor):
        if self.saldo < valor:
            print("saldo insuficiente!")
            return False
        else:
            self.saldo = self.saldo - valor
            print(f"Saque no valor de R${valor} realizado com sucesso!")
            return True
            

ContaHelmer = ContaBancaria("helmer", 100)

ContaHelmer.depositar(100)
print(ContaHelmer.saldo)
ContaHelmer.sacar(20)
print(ContaHelmer.saldo)        

# 6. Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.
print(ContaHelmer.sacar(30))
print(ContaHelmer.sacar(500))
# 7. Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f"Nome do Aluno: {self.nome}\nNota do Aluno: {self.nota}"
    
class Turma:
    
    lista_alunos = []

    def adicionar_aluno(self,aluno):
        self.lista_alunos.append(aluno)

turma1 = Turma()

helmer = Aluno("helmer", 10)
ana_clara = Aluno("Ana Clara", 7.8)

turma1.adicionar_aluno(helmer)
turma1.adicionar_aluno(ana_clara)

for aluno in turma1.lista_alunos:
    print(aluno)

# 8. Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
#feito.

# 9. Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.
class Cachorro:
    especie = "Canis familiaris"

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


print(f"Acessando pela classe: {Cachorro.especie}")

doguinho = Cachorro("princesa", 2)

print(f"Acessando pelo objeto: {doguinho.especie}")