#1
lista = [1,"um",[1,2,3]]

#2
lista.append("dois")
lista.append("tres")
lista.pop(0)

#3
lista2 = lista.copy()
print(id(lista))
print(id(lista2))

#4
lista = [1,2,3,4,5]
lista_multiplicacao = []
cont = 0

while cont < 5:
    lista_multiplicacao.append(lista[cont] * 5)
    cont+=1

print(lista_multiplicacao)


#5
list = [ 1,2,3,4,5,6]
print(list[3:5])

