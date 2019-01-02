#Estrutura de controle

nota1 = int (input("Digite sua nota: "))
media = 6

'''
: dois pontos em python é uma chave, quando pressiona o botão enter
o bloco if vai indentar sozinho
'''
if nota1 > media:
    print("Aprovado")

elif nota1 == media:
     print ("DP")
     
else:
    print("Reprovado")
