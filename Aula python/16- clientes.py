cliente = input("Qual é o nome do cliente: ")
valor = int(input("Qual foi o total comprado: "))

if valor >=5000:
    print(f"O cliente: {cliente}. cliente de ouro")

elif valor >= 2000 and valor <=5000:
    print(f"O cliente: {cliente}. cliente prata")

else:
    print(f"O cliente {cliente}.cliente bronze")