
lista1 = [0,1,2,3,4,"Jair","Ortega",2009]
lista2 = [4,1,5,2,"Alejandro","Cañar",2009]


conjunto1 = set(lista1)
conjunto2 = set(lista2)

lista_union = list(conjunto1 | conjunto2)


lista_solo_primera = list(conjunto1 - conjunto2)


lista_solo_segunda = list(conjunto2 - conjunto1)


lista_ambas = list(conjunto1 & conjunto2)


print("Elementos de las dos listas:", lista_union)
print("Solo en la primera lista:", lista_solo_primera)
print("Solo en la segunda lista:", lista_solo_segunda)
print("Elementos que aparecen en ambas:", lista_ambas)