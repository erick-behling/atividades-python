consumo = float(input("Consumo em kWh: "))

#SE condição
#SENAO SE condição
#SENAO SE condição
#FIMSE

if consumo > 300:
    print("Classificação: muito alto.")
elif consumo > 200:
    print("Classificação: alto.")
elif consumo > 100:
    print("Classificação: normal.")
else:
    print("Classificação: baixo.")