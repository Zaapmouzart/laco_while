from time import sleep
#While


""" tentativas = 0
while tentativas <5:
    print("Tente novamente")
    tentativas += 1  """

senha_pessoal = ""
while senha_pessoal != "joao_lucas":
    senha_pessoal= input("Digite sua senha ")
    if senha_pessoal!= 'joao_lucas':
        print("Senha incorreta ")
    else:
        break
print ("Bem vindo ")