#Aula 10 - Estruturas de dados

'''Estrutura de dados em python pode ser

      - List - o indice sempre começa com 0
      - Tuples
      - Set
      - Dictionary
'''

#List

lista1 = [1, 'Antonio', 3.14, 'Nova string', True]

lista1[2] = 'PI'


''' Incluir um novo valor na lista '''
lista1.append('Novo Valor')


''' Remover um valor na lista '''
lista1.pop()

''' Remover um valor especifico '''
lista1.remove('Antonio')

''' Inserir um novo item na lista '''
lista1.insert(2, 'Insert')
lista1.insert(0, 'Inicio')

''' Imprimir a lista inversa '''
lista1.reverse()

lista1.remove(1)

''' Lista Sort - não pode ter string e inteiros na lista, organiza a lista
em oridem alfabetica'''
lista1.sort()

''' Lista Sort ordem inversa '''
lista1.sort(reverse = True)

for x in lista1: print(x)


#Tuples -Não mutaveis
tupla = (3, 4, 'Nome')

tupla2 = 3, 5, 'Nome', 'Sobrenome'

#Set - Não permite repetições
s = set()

s

''' Adicionar valor'''

s.add(1)

s.add(12)

s.add(13)

s.add(14)


''' Remover valor'''
s.pop()

s.remove(13)

#Dictionary - estrura de dados que permite armazenar valores com uma chave e um valor

'''Dicionario vazio'''
d = {}

''' Verificar tipo do dicionario'''
type(d)

'''Inserir valores no dicionario '''
d['nome'] ="Marcos"
d['Sobrenome'] = "Almeida"

d['data_nascimento'] = '15/09/1983'
d['telefone'] = '1196941441'


''' Tirar chave que mostra telefone '''
d.pop('telefone')

d.popitem()

''' Valores que estão no dicionario'''
d.values()

d.keys()
































