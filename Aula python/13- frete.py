compra = int(input("Qual é o valor da compra: "))

if compra >=300:
    print(f"O valor com {compra} tem: Frete grátis")

else:
    print(f"O valor com: {compra} fica esse total: {compra + 25}")