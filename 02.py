'''
2)Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    nome = input("Digite seu nome: ").lower()
    senha = input("Digite sua senha: ").lower()

    if nome != senha:
        print("Dados salvos.")
        break
    else:
        print("Nome de usuário e senha não podem ser iguais. Tente novamente.")
