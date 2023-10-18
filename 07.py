'''
7)Faça um programa que leia 5 números e informe o maior número.
'''
lista = [0] * 5
for x in range(5):
    lista[x] = int(input(f"Digite o {x+1}º valor: "))

maior = lista[0]
for x in range(1, 5):
    if lista[x] > maior:
        maior = lista[x]
print(f"Maior valor foi = {maior}")

