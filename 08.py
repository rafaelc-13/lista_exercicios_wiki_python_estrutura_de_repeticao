'''
8)Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
lista = [0]*5
soma = 0
cont = 0

for x in range (5):
    lista[x]= int(input(f"{x+1}º valor: "))
    soma += lista[x]
    cont += 1

media = soma/cont
print(f"A soma dos valores é {soma}.\n"
      f"A média dos valores é {media}.")
