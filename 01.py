'''1)Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

nota = int(input("Digite uma nota entre 0-10: "))

while nota>10 or nota<0:
    nota = int(input("Valor inválido. \n"
                     "Digite uma nota entre 0-10: "))
else:
    print("Boa!")
