#Manipulação de arquivos texto

'''
r - Leitura
w - Escrita
a - apend
r+ - leitura e escrita


#Leitura do arquivo pessoas
arquivo = open('pessoas.txt','r')
print(arquivo)

#Ler o conteudo do arquivo txt
for linha in arquivo:
      print(linha)
'''

#Encapsular em uma função
def ler_arquivo(nome_arquivo):
      arquivo = open(nome_arquivo, 'r')

      for linha in arquivo:
            print(linha)

      arquivo.close()

      
#Salvar Arquivo
def salvar_arquivo(nome_arquivo, texto):
      arquivo = open(nome_arquivo, 'w')
      arquivo.write(texto)

      arquivo.close()
