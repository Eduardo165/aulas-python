salario = float(input("Digite o salario do cliente: "))
parcela = float(input("Digiteo valor da parcela: "))

if parcela <= salario*0.30:
    print("Emprestimo aprovado")

else:
    print("Emprestimo nao aprovado.")