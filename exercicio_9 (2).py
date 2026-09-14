leituras = []

while True:
    print("\n1 - Registrar leitura\n2 - Ver relatório\n3 - Listar leituras\n0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Valor da leitura (kWh): "))

        if valor <= 0:
            print("Valor deve ser positivo.")
        else:
            leituras.append(valor)
            print("Leitura registrada.")

    elif opcao == "2":
        if not leituras:
            print("nenhuma leitura registrada.")
        else:
            print(f"Quantidade: {len(leituras)}")

            media = 0
            for i in range(len(leituras)):
                media = media + leituras[i]

            media = media / len(leituras)
            print(f"Média: {media:.2f}")
            print(f"Maior: {max(leituras)} kWh")
            print(f"Menor: {min(leituras)} kWh")

    elif opcao == "3":
        if not leituras:
            print("Nenhuma leitura registrada.")
        else:
            for i in range(len(leituras)):
                print(f"{i + 1} - {leituras[i]} kWh")

    elif opcao == "0":
        print("Encerrando.")
        break

    else:
        print("opção inválida.")