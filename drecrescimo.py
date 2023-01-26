"""Crie um laço que imprima na tela uma contagem decrescente de 100 a 1"""
from time import sleep
contador = 100

while contador >=0:
    print(contador)
    contador -=1
    sleep(0.2)
print("A contagem foi finalizada ")