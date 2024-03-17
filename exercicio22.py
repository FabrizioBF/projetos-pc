'''
Construir duas listas: l1 e l2
'''
l1 = []
l2 = ["Pernambuco","PE","Pe"]

l1.append("Re")
l1.append("ci")
l1.append("fe")

print(l1[0])

l1.remove("Re")

print('Tamanho da lista l1: ', len(l1))

l1.insert(0, "Re")

print('Tamanho da lista l1 depois da inserção de um novo elemento: ', len(l1))

print('Lista 2:', l2)
