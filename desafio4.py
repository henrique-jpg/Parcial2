# Solicita o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação foi escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    # Verifica divisão por zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero")
        resultado = None
else:
    print("Operação inválida")
    resultado = None

# Exibe o resultado se for válido
if resultado is not None:
    print("Resultado:", resultado)