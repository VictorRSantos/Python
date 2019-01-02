#Modulos
#precisamos importar random
'''
Vamos utilizar algumas funções da api random

'choice', 'randint', 'random', 'shuffle'

'''

#import
import random


#random - gera número aleatorios
random.random()

#random.randint - gera número aleatorios entre 10 e 20
random.randint(10, 20)

#random.choice - pode criar uma lista, e o choice vai apresentar um nome aleatorio dentro da lista
x = ['gol','astra','fusca','palio','uno']
random.choice(x)

#random.suffle - Enbaralha a lista; Ex:x = ['gol','astra','fusca','palio','uno']
x = ['gol','astra','fusca','palio','uno']
random.shuffle(x)

#Modulo de string - vamos importar String
import string

#string.punctuantion - Traz uma string com todos os caracteres especiais
string.punctuation #Retorna - '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.digits #Retorna - '0123456789'
string.hexdigits #Retorna - '0123456789abcdefABCDEF'
string.capwords("teste de capitalize no curso de python") #Retornar 'Teste De Capitalize No Curso De Python'
