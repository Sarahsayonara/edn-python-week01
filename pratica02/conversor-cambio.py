# 1- Conversor de Moeda 
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
#T axa do dólar: R$ 5.20
# Taxa do euro: R$ 6.15 
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

valor_em_dolares = round(valor_em_dolares, 2)
valor_em_euros = round(valor_em_euros, 2)

print(f"Valor em dólares: ${valor_em_dolares}")
print(f"Valor em euros: €{valor_em_euros}")