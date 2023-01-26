"""Crie um loop pque ira continuamente pedir 
ao usúario para digitar a senha e só ira permitir 
quando a senha digitada for "secreto" """

senha = ""

while senha != "secreto":
    senha =input("Digite sua senha ")
    if senha != "secreto":
        print("Senha incorreta ")

    else:
        break
print("Seja bem vindo ao portal")