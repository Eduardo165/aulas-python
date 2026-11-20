ano_atual = float(input("Digite o seu ano atual: "))
nascimento = float(input("Digite sua data de nascimento: "))

idade = ano_atual-nascimento

if idade >18:
    print("Maior de idade")

else:
    print("Menor de idade")


print(f"Ah sua idade é :{idade}")

input("Pressione o Enter para finalizar")