valor = float(input("Qual é o valor da compra: "))
pagamento = input("Digite a forma de pagamento")

if pagamento == "Pix":
    print(f"Pagamento com o PIX tem o desconto de 10% de {valor} vai ficar pelo total de {valor - 0.10}")
elif pagamento == "Dinheiro":
    print(f"O Pagamento com dinheiro tem o desconto de 5% de {valor} vai ficar pelo total de {valor - 0.05}")
elif pagamento == "Cartao":
    print(f"Pagamento com cartao nao tem desconto de {valor} vai ficar pelo total de {valor}")
