"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações. """

senha = ""
nome_usuario = ""

while senha == nome_usuario:
    nome_usuario= input("Digite seu nome de usúario")
    senha = input("Digite uma senha ")
    if senha == nome_usuario:
        print("Senha inválida, digite uma nova senha ")
    else: break

print("Usuário cadastrado com sucesso")

