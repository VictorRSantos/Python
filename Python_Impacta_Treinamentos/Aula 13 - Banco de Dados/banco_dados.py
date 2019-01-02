#Banco de Dados
import sqlite3

#Vamos criar uma variavel para armazenar a conexão com o banco de dados
conn = sqlite3.connect("galeria.db")

#Vamos criar um cursor, são interadores aonde permite navegar e maipular os registro do banco de dados
cursor = conn.cursor()

#Sempre vamos  cada script dentro de uma função para não correr o risco de executar mais de uma vez o script

#Criar Tabela
def criar_tabela():
      sql = """
      CREATE TABLE albums(titulo text, artista text, data_lancamento  text,
      data_publicacao text, midia text)

      """
      #Vamos executar um comando SQL
      cursor.execute(sql)
      #Sempre usar o commit para confirmar alteração no banco
      conn.commit()


#Função Insert
def grava_album():
      sql = "INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '24/04/2012', 'Xplore Records','MP3')"

      cursor.execute(sql)

      conn.commit()


#O comado executemany,  Serve para inserir varios registros no banco de dados
def grava_muitos():
      albums = [
                        ('Exodus', 'Andy Hunter', '9/7/2002 ', 'Sparrow Records', ' CD') ,
                        ('Until We Have Faces', ' Red', ' 1/2/2011', 'Essential Records', 'CD')
                      ]
      cursor.executemany("INSERT INTO albums VALUES(? , ? , ? , ? , ?)", albums)

      conn.commit()


#Update - Alterar Registro da tabela
def atualiza():
      sql = """
      UPDATE albums SET artista = 'John Doe'
      WHERE artista = 'Andy Hunter'
      """

      cursor.execute(sql)

      conn.commit()

#Excluir Registro - Delete
def excluir():
      sql = """
               DELETE FROM albums
               WHERE artista = 'John Doe'
               """

      cursor.execute(sql)

      conn.commit()

#Listar

def listar():
      sql = """
      SELECT rowid, * FROM albums ORDER BY artista
      """

      cursor.execute(sql)

      #Para listar precisamos fazer um for - (fetchall) vai ficar responsavel para trazer toda a tabela que estamos pesquisando
      for row in cursor.fetchall ():
            print (row)
      
      
































