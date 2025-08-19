#listas, tuplas e dicionários

frutas = ["Limão","Banana","Morango","Coco"]

#adiciona elemento de acordo com o index escolhido
frutas.insert(1,"Laranja")
print(frutas)

#adiciona elementos ao final da lista
frutas.append("kiwi")
print(frutas)

#adiciona uma lista na outra
frutas_vermelhas = ["cereja","amora","framboesa"]
frutas+=frutas_vermelhas
print(frutas)

#remover elementos pelo nome
frutas.remove("Morango")
print(frutas)

#remove elemento pelo index
frutas.pop()
print(frutas)

#deletando listas
del frutas[1:2]

#slice lists
print(len(frutas))
frutas2 = frutas[1:5]
print(frutas2)


#copiando listas
frutas_copia = frutas[:] #fazendo copia do conteudo da lista toda
frutas_copia = frutas.copy() #outro modo é utilizando o metodo copy

frutas.sort() #ordena a lista numeriamente ou alfabeticamente
frutas.reverse() #ordena inversamente


