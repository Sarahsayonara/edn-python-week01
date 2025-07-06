def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor = calcular_gorjeta(100, 10)
print(f"Gorjeta: R${valor:.2f}")