#String
"Marcos"

'Antonio'

'''
Texto Multilinha
para teste
na aula de python

'''
'\nTexto Muitilinha\npara teste\nna aula de python\n'

#Acessando indice do texto
"Texto para ser fatiado"[0 : 6]     #Ex: "Texto "
"Texto para ser fatiado"[0 : 10]   #Ex: "Texto para"
"Texto para ser fatiado"[3 : 10]   #Ex: "to para"
"Texto para ser fatiado"[: 10]      #Ex: "Texto para "
"Texto para ser fatiado"[0 : ]      #Ex: "Texto para ser fatiado"
#steps
"Texto para ser fatiado"[0: 10 : 3] #Ex: 'Ttpa'

"Fatiamento com valor negativo" [3 : -4] #Ex: iamento com valor nega

"Fatiamento com valor negativo" [: : -1] #Ex: ovitagen rolav moc otnemaitaF

#################################################################

nome = "Marcos"

nome = 'B' + nome[1 : ] #Resultado: Barcos (B substitui a letra M

nome.startswith('B') # Verifica se é verdadeiro o falso

# Fazer a troca da letra r pelo 3, mais não altera o valor da variavel nome. Por que só faz uma copia
nome.replace('r', '3')  #Ex: Ba3cos

#Trocando o valor da variavel 
nome = nome.replace('r' , '3')


#Split - Espaço
texto = "Testando split no python"
s = texto.split() #Resultado ['Testando',  'split', 'no',  'python']
texto = "Testando;novos;delimitadores"


#Join
data = ['18','05','1979']

'/'.join(data) #Resultado: '18/05/1979'

































