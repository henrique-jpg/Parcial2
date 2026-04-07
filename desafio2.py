# Solicita um número inteiro ao usuário
numero = int(input("Digite um número: "))

# Verifica se o número é par usando o operador %
if numero % 2 == 0:
    # Se o resto da divisão por 2 for 0, é par
    print("O número é par")
else:
    # Caso contrário, é ímpar
    print("O número é ímpar")