'''
12)Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser uma abaixo da outra.
'''
x = int(input("Vamos descobrir a tabuada de: "))

for y in range (1,11):
    print(f"{x} * {y} = {x * y}")
