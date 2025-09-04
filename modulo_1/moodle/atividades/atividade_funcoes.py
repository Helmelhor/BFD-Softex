# 1. Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.
def saudacao():
    print("Olá, bem-vindo ao Python!")

saudacao()

# 2. Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.
def dobro(numero):
    return numero * 2

print(dobro(5))
print(dobro(10))

# 3. Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.
def soma(a, b):
    return a + b

print(soma(10, 20))

# 4. Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:
#    "Olá, [nome]!"
#    Caso o nome não seja informado, mostre "Olá, visitante!".
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")

mensagem("Ana")
mensagem()

# 5. Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

print(operacoes(10, 5))

# 6. Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.
def media(*args):
    return sum(args) / len(args) if args else 0

print(media(10, 20, 30))
print(media(5, 15, 25, 35, 45))
print(media(1, 2, 3, 4, 5, 6, 7))

# 7. Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
#    dados_pessoais(nome="Ana", idade=25, cidade="Recife")
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")

# 8. Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.
def calculadora(a, b, operacao):
    def somar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y

    def multiplicar(x, y):
        return x * y

    def dividir(x, y):
        return x / y if y != 0 else "Divisão por zero não permitida"

    if operacao == "soma":
        return somar(a, b)
    elif operacao == "subtracao":
        return subtrair(a, b)
    elif operacao == "multiplicacao":
        return multiplicar(a, b)
    elif operacao == "divisao":
        return dividir(a, b)
    else:
        return "Operação inválida"
print(calculadora(10, 5, "soma"))
print(calculadora(10, 5, "subtracao"))
# 9. Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:
#    def soma(a, b): return a + b
#    aplicar_operacao(3, 4, soma)
def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

def soma(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(3, 4, multiplicar))