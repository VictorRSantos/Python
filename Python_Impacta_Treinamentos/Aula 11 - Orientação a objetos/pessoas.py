#Orientação a objetos

'''
. Classes
.Atributos
.Métodos
.Objetos
.Herença
.Polimorfismo
'''

# Classes

class Pessoa (object):

      nome = None
      
      def salvar(self, x): #Self  - identifica a propria classe
            
            self.nome = x
            
            print("Salvando", self.nome)

