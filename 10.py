'''
10)Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))

for x in range (n1,n2+1):
    print (x,end=" ")
