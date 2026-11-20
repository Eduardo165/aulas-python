
tempo = float(input("Digite quantos grau esta agora na sua cidade:"))

if tempo >=30.0:
    print("Esta bastante calor.")

elif tempo >=20.0 and tempo <=29.9:
    print("O clima esta agradavel.")

elif tempo >=10.0 and tempo <19.9:
    print("Esta bastente frio.")

else:
    print("Temperatura não Encontrada.")