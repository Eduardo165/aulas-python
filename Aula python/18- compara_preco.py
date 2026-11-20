nome1 = input("Fornecedor 1: ")
valor1 = float(input("Valor: "))

nome2 = input("Fornecedor 2: ")
valor2 = float(input("Valor: "))

if valor1 < valor2:
    print(nome1, "tem o menor preço")

elif valor2 < valor1:
    print(nome2, "tem o menor preço")

else:
    print("As propostas possuem o mesmo valor")