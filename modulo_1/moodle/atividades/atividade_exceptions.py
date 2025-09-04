 # 1. Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

# try:
#     num = int(input("Digite um número inteiro: "))
# except:
#     print("Digite um número INTEIRO!!!")


# 2. Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

# def multiplicacao(num1,num2):
#     return num1 * num2

# try:
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite um número: "))
#     print(multiplicacao(num1,num2))
# except:
#     print("Dado inválido, digite um número rapaz!!")


# 3. Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

# try:
#     num = int(input("digite um numero inteiro: "))
# except:
#     print("Digite um numero válido !!!")
# else:
#     print("Conversão bem-sucedida!!!!!!!!!!")


# 4. Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

import os

try:
    os.open("dados.txt")
except:
    print("ocorreu algum erro com o arquivo importado.")
finally:
    print("fim da verificação")

# 5. Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

# def dividir(a,b):   
#         if b == 0:
#             raise ZeroDivisionError(f"Você não pode dividir {a} por ZERO!")
#         else:
#             return a / b
    
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um número: "))

# print(dividir(num1,num2))


# 6. Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.



# 7. Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
#    ValueError se o usuário digitar algo inválido
#    ZeroDivisionError se tentar dividir por zero
#
# 8. Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
#    try para a conversão,
#    else para verificar se é par ou ímpar,
#    finally para exibir "Fim do programa".
#
# 9. Crie uma função sacar(saldo, valor) que:
#    Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
#    Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
