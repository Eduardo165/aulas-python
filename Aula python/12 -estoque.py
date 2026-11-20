produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade disponivel no estoque: "))

if quantidade <=10:
    print("O estoque esta critico")

elif quantidade <=30:
    print("Estoque baixo")

else:
    print("Estoque adequado")

