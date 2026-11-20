import os
os.system("cls")



nome = input("Digite o nome do vendedor: ")
vendas = float(input("Digite o valor das vendas: "))

if vendas >= 20000:
    percentual = 10

elif vendas >= 10000:
    percentual = 7

else:
    pecentual = 5


comissao = vendas/10
comissao2 = vendas/7
comissao3 = vendas/5

print(f"Vendedor: {nome}")
print(f"total vendido: R$ {vendas: .2f}")
print(f"E a sua comissao vai ser: {comissao}")