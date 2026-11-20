nome = input("Digite seu nome: ")

nota1 = float(input("Digite sua nota primeira nota: "))
nota2 = float(input("Digite sua nota segunda nota: "))
nota3 = float(input("Digite sua nota terceira nota: "))

soma = nota1+nota2+nota3
media= soma/3

if media >=7.0 and media <=10:
    print(f"O aluno {nome} foi aprovado. A media do aluno foi {media:.2f}")

elif media >=4.0 and media <=6.9:
    print(f"O aluno {nome} precisa realizar recuperação. A media do aluno foi {media:.2f}")


else:
    print(f"O aluno {nome} foi REPROVADO. A media foi {media:.2f}")

