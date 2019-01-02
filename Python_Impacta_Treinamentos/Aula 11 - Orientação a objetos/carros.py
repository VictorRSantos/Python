'''Declarando a classe'''
class Carro(object):

      '''Método Construtor '''      
      def  _init_(self, caminho) :            
            self.caminho = caminho

      
      '''Metodo'''
      def  andar (self) :
            print('Andando pela', self.caminho)



class Fusca(Carro):
      

            def __init__ (self, caminho):
                  self.caminho = caminho

            def correr(self):
                  self.caminho = "pista"
                  super(Fusca, self).andar()



class Ferrari(Carro):

      def _init_ (self, caminho):
                        
            self.caminho = caminho

      def andar(self):
            print("Correndo muito ")
