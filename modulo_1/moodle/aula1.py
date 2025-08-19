#1
num = "123"
print(int(num))
print(float(num))

#2
msg = "Python é incrível"
print(len(msg))
print(msg.upper()) # Deixa tudo em maiúsculas
print(msg.replace("incrível", "poderoso")) # Troca "incrível" por "poderoso"

#3

numeros = [10,20,30,40,50]

print(f"terceiro elemento: {numeros[2]}")
numeros.append(60)
numeros.remove(20)
print(numeros)

#4
aluno = {"nome": "maria","idade":"22","curso":"engenharia"}
aluno["notas"]=[8.5,7.0,9.2]
print(aluno["curso"])

#5
cores = ("vermelho", "verde", "azul", "verde")
cores_unicas = tuple(set(cores))
cores_unicas = cores_unicas + ("amarelo",)
print(cores_unicas)
