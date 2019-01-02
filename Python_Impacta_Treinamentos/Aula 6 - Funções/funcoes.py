#Aula 6 - Funções

'''Função sem retorno no prompt so chamar
   somar(em passar valor das variaveis)
   Exemplo:
   somar(1,2)      
'''
def somar (numero1, numero2):
    print( numero1 + numero2)


'''Função com Retorno '''
def subtrair(n1, n2):
      return n1 - n2

'''
**kwargs - Mapa dicionario do Python que ira converte os
paramentros passado na chamada da função em um dicionario para chamada correta

'''

def imprime_parametros(**kwargs):
      for key, value in kwargs.items():
            print( "%s = %s" % (key, value))

def func1(param1):
      pass


def calcular_media() :
      
      n1 = int (input("Digite note n1:"))
      n2 = int (input("Digite nota n2: "))
      n3 = int (input("Digite note n3: "))

      media = (n1 + n2 + n3) / 3
      
      return media  
