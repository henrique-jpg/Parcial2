# Solicita o tempo em segundos
segundos = int(input("Digite o tempo em segundos: "))

# Calcula as horas
horas = segundos // 3600

# Calcula o restante dos segundos
resto = segundos % 3600

# Calcula os minutos
minutos = resto // 60

# Calcula os segundos restantes
segundos_restantes = resto % 60

# Exibe o resultado formatado
print("Tempo convertido:")
print(horas, "hora(s),", minutos, "minuto(s),", segundos_restantes, "segundo(s)")