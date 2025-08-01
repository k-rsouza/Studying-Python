tupl = (1, 2, 3, 4, 5)

lista = [1, 2, 3, 4, 5]

c = lista.count(3) 
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

for valor, item in pessoa.items():
    print(f'{valor} = {item}')      
print('\n lista com len')
lista = ['a', 'b', 'c', 'd', 'e']
for i in range(len(lista)):
    print(f'Índice {i} = {lista[i]}')