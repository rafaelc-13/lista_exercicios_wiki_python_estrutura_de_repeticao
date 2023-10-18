'''
11)Altere o programa anterior para mostrar no final a soma dos números.
'''
n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))
soma = 0

for x in range (n1,n2+1):
    soma += x
print(f"A soma dos valores inteiros entre {n1} e {n2} é: {soma}")
