# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
# Operação inválida
# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        
        num2 = float(input("Digite o segundo número: "))
        
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")
        
        if operacao == '/' and num2 == 0:
            raise ZeroDivisionError("Erro: divisão por zero.")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

        print(f"Resultado: {resultado}")
        break

    except ValueError as ve:
        print(f"Erro: {ve}. Tente novamente.\n")
    except ZeroDivisionError as zde:
        print(f"{zde} Tente novamente.\n")