
produto = input('Produto: ')
preco = float(input('Preço: '))
porcentagem = int(input('Porcentagem de desconto: '))
desconto = preco * (porcentagem/100)
valor_desconto = preco - desconto
print(f'O {produto} com {porcentagem}% de desconto custará R${valor_desconto}')