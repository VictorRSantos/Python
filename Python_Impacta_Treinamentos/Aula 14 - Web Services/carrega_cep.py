import requests
import json
from enderecos import Endereco

#Usuário entrar com CEP
cep = input("Digite um CEP: ")

'''Chamar o serviço com a bibliioteca requests e vamos verificar se 
o status é [200] caso seja de sucesso vamos montar nosso objeto
e salvar no banco de dados. Caso contrario imprimir um mensagem de
aviso para usuário
'''
r = requests.get("https://viacep.com.br/ws/%s/json/" % cep)

#Verificar status
#Regra para salvar no banco de dados
if r.status_code == requests.codes.ok:
   
    j = json.loads(r.text)

    #Montar nosso objeto
    endereco = Endereco()
  
    #Vamos abastecer seus atributos
     #Vamos abastecer seus atributos
    endereco.cep = j['cep']
    endereco.logradouro = j['logradouro']
    endereco.complemento = j['complemento']
    endereco.bairro = j['bairro']
    endereco.localidade = j['localidade']
    endereco.uf = j['uf']
    endereco.unidade = j['unidade']
    endereco.ibge = j['ibge']
    endereco.gia = j['gia']

    endereco.salvar()

else:
    print("Cep não encontrado")

#Montar nosso objeto, vamos importar o modulo Json
