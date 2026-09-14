consumo = 185
Consumo = 190
CoNsUmO = 200
TARIFA = 0.85

custo = consumo * TARIFA
print(f"Custo estimado: R${custo:.2f}")

# Consumo e consumo são duas variáveis diferentes porque o Python é case-sensitive
# O dois-pontos (:) avisa que será aplicada uma formatação especial àquela variável. No caso, ela vai ter apenas 2 casas atrás da vírgula (.2f). O 2 é o número casa e o f é de FLOAT (número com vírgula)