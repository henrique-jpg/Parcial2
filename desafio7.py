# Solicita o capital inicial
capital = float(input("Digite o capital inicial: "))

# Solicita a taxa de juros (em %)
taxa = float(input("Digite a taxa de juros (%): "))

# Solicita o tempo (em meses ou anos)
tempo = float(input("Digite o tempo: "))

# Calcula os juros simples
juros = capital * (taxa / 100) * tempo

# Calcula o montante final
montante = capital + juros

# Exibe os resultados
print("Juros:", juros)
print("Montante final:", montante)