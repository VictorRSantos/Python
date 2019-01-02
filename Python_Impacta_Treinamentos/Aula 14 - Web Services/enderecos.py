import sqlite3

class Endereco(object):

#Vamos encapsular dentro do metodo _init_
    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.unidade = None
        self.ibge = None
        self.gia = None
    
    #Criar função para criar Tabela
    def cria_tabela(self):
        conn = sqlite3.connect("enderecos.db")
        cursor = conn.cursor()

        #IF NOT EXISTS não permite criar a tabela endereco novamente
        cursor.execute('''   
            CREATE TABLE IF NOT EXISTS endereco(
                cep text, logradouro text, complemento text, 
                bairro text, localidade text, uf text, unidade text,
                ibge text, gia text)        
        ''')

        conn.commit()


    #Função Salvar
    def salvar(self):
        self.cria_tabela()

        conn = sqlite3.connect("enderecos.db")
        cursor = conn.cursor()


        cursor.execute("INSERT INTO endereco VALUES ('%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s')" % 
        (self.cep, self.logradouro, self.complemento,
        self.bairro, self.localidade, self.uf, self.unidade, self.ibge, self.gia))

        conn.commit()


    
