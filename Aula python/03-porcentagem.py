import os
os.system("cls")

produto=input("Qual é o produto: ")
preco=float(input("Digite o valor do produto: " ))
desconto=float(input("Digite o valor do seu desconto: "))
porcentagem=float(input("Qual e porcentagem de desconto: "))

porcentagem = desconto*preco/100

print(f"O produto{produto} com o valor de R${preco}, agora com o desconto de R${porcentagem} ficou com o total de R$ {preco-porcentagem }")
