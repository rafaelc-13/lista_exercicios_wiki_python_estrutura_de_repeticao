'''
3)Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'
'''

while True:
    opcoes_sexo = ("f","m")
    opcoes_estado_civil = ('s', 'c', 'v', 'd')

    nome = input("Digite seu nome: ")
    while len(nome) <= 3:
        print("Nome inválido, deve possuir mais de 3 letras.")
        nome = input("Digite seu nome: ")

    idade = int(input("Digite sua idade: "))
    while idade <= 0 or idade > 150:
        print("Idade inválida. Deve ser entre 1-150.")
        idade = int(input("Digite sua idade: "))

    salario = float(input("Digite seu salario: "))
    while salario <= 0:
        print("Você não está desempregado. Quanto ganha de verdade?")
        salario = float(input("Digite seu salario: "))

    sexo = input("Sexo (M/F): ").lower()
    while sexo not in opcoes_sexo:
        print("Por favor responda no formato exposto (M/F).")
        sexo = input("Sexo (M/F): ").lower()

    estado = input("Estado civil : \n"
                   "s - solteiro\n"
                   "c - casado\n"
                   "v - viuvo\n"
                   "d - divorciado\n"
                   ":").lower()
    while estado not in opcoes_estado_civil:
        print('Favor indicar estado apenas com uma das letras abaixo: ')
        estado = input("Estado civil : \n"
                   "s - solteiro\n"
                   "c - casado\n"
                   "v - viuvo\n"
                   "d - divorciado\n"
                   ":").lower()
    print("Dados Cadastrados!")
    break









