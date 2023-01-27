"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
 e continue pedindo até que o usuário informe um valor válido, ou digite a tecla para sair do programa. """

media = 0
while True:
    media = float(input("Digite sua média "))
    if media >=6 and media<=10:
        print(f"Parabéns, você esta aprovado sua média é {media} ")
    elif media <6 and media >= 0:
        print(f"Você foi reprovado, sua média é {media}")
    else:
        print("Média invalida ") 
        
    
    sair =(input("Digite S para sair ou N para continuar no Programa"))
    if sair == "S" or sair =="s":
        break
    elif sair == "N" or sair == "n":
       pass

print(" Programa executado com sucesso")
        