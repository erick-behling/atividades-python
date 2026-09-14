nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2
print(f"Média: {media:.1f}")

#if é o equivalente do SE-FIMSE do Portugol. Repare o uso dos dois pontos na expressão
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")