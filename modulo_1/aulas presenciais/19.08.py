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
numeros = [1,2,3]
soma = (numeros[0] * 5) + (numeros[1]*5) + (numeros[2]*5)
lista_soma = [soma]

#5
list = [ 1,2,3,4,5,6]
print(list[3:5])

