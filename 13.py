'''
13)Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
 Não utilize a função de potência da linguagem.
'''
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
result = 1

for x in range (expoente):
    result = result * base
print(f"{base} elevado a {expoente} é {result}")
