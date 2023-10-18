'''
4)Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que
a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
A = 80000
B = 200000
anos = 0

while A < B:
    taxa_crescimento_A = 0.03 * A
    taxa_crescimento_B = 0.015 * B
    A += taxa_crescimento_A
    B += taxa_crescimento_B
    anos += 1

print (f"Os países estão iguais \n"
       f"Com {A} habitantes para o país A.\n"
       f"{B} habitantes para o país B. \n"
       f"Isso aconteceu em {anos} anos.")
