lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

print(lenguajes[1])

#ordenar elementos
lenguajes.sort()
print(lenguajes)

#acceder a un elemnto dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]} '
print(aprendiendo)

#modificar valores de una lista
lenguajes[2] = 'C#'
print(lenguajes)

#Agregar Elementos a un lista
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar de la Lista
del lenguajes[1]
print(lenguajes)

#Eliminando elementos de la Lista con pop()
lenguajes.pop() #si no se define nada elimina el ultimo
print(lenguajes)
lenguajes.pop(0) #indicandole, elimina el seleccionado
print(lenguajes)

#eliminando por el nombre del elemento
lenguajes.append('PHP')
print(lenguajes)
lenguajes.remove('C#')
print(lenguajes)
