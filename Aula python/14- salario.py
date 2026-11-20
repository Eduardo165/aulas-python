nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salario atual: "))




if salario <=2000:
    print(f"O seu salario tera um aumento de {salario*0.10}")

elif salario <=5000:
    print(f"O seu salario tera um aumento de {salario +0.07}")

else:
    print(f"O seu salario tera um aumento de {salario +0.05}")
