nome = input("Digite seu nome: ")
ano_atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano_atual-nascimento

print(f"A sua idade é: {idade} anos")

if idade >=18:
    print("Maior de idade")
    cnh = input(f"Voce possui carteira de motorista {nome}?: ")
    if cnh == 'sim':
        print(f'Voce pode dirigir {nome}')

    else:
        print(f"Voce não pode dirigir {nome}")

else:
    print("menor de idade")
