'''
5)Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

while True:
    A = int(input("Qual a população do país A? "))
    B = int(input("Qual a população do país B? "))
    taxa_A = float(input("Qual a taxa de crescimento da população de A ao ano? (0-100%) "))
    taxa_B = float(input("Qual a taxa de crescimento da população de B ao ano? (0-100%) "))

    if A <= B or taxa_A <= taxa_B:
        print("Por favor, insira valores válidos. A população de A deve ser menor que a de B e a taxa de crescimento de A deve ser maior que a de B.")
        continue

    anos = 0

    while A < B:
        taxa_crescimento_A = taxa_A * A / 100
        taxa_crescimento_B = taxa_B * B / 100
        A += taxa_crescimento_A
        B += taxa_crescimento_B
        anos += 1

    print(f"Os países estão com suas populações mais próximas. \n"
           f"Com {A:.0f} habitantes para o país A.\n"
           f"{B:.0f} habitantes para o país B. \n"
           f"Isso aconteceu em {anos} anos.")

    repetir = input("Deseja realizar outra simulação? (S/N): ")
    if repetir.lower() != 's':
        break
