"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
 para então calcular e mostrar o valor do troco. Após esta operação, 
 o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
 A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara 
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
"""

produto1 = 0
produto2 = 0
produto3 = 0
final_da_compra = ""

print("SUPERMERCADO TABAJARA")

while True:
    produto1 = float(input("Digite o valor do produto "))
    produto2 = float(input("Digite o valor do produto "))
    produto3 = float(input("Digite o valor do produto "))
    final_da_compra = input("Cliente finalizou a compra? S/N ")
    
    if final_da_compra == "S" or final_da_compra == "s":
        total = produto1 + produto2 + produto3
        print(f" Valor total é de RS{total}")
        valor_pago = float(input("Digite o valor pago pelo cliente "))
        troco = valor_pago - total


        print("-" * 50)
        print("SUPERMERCADO TABAJARA")
        print("-" * 50)

        
        print(f"Produto 1 = R${produto1}")
        print(f"Produto 2 = R${produto2}")
        print(f"Produto 3 = R${produto3}")
        print(f" Valor total é de RS{total}")
        print(f"Cliente pagou em dinheiro a quantia de R${valor_pago}")

        print("*" * 30)
        print(f"Recebeu o troco de R${troco:.2f}") 
        print("*" * 30)
        
        print("Obrigado!! Volte sempre")
        sair_programa = int(input("Digite 0 para encerrar o programa"))
        if sair_programa == 0:
            break
        else:pass


    elif final_da_compra=="N" or final_da_compra=="n":
        print("Por favor retorne quando finalizar  compra ")

    else:
        print("Digite S para cliente com compra finalizada, ou N para compra não finalizada") 

print("Obrigado por utilizar os serviços Tabajara")

    
    
        


     
    

