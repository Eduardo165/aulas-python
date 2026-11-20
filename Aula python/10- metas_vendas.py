nome = input("Digite o nome do vendedor: ")
vendas = float(input("Digite o total vendido no mes: "))

if vendas >= 15000:
    desempenho = "Excelente"

elif vendas >= 10000:
    desempenho = "Meta atingida"

else:
    desempenho = "Meta nao atingida"

print(f"Vendedor: {nome}")
print(f"total vendido: R$ {vendas: .2f}")
print(f"Desempenho: {desempenho}")