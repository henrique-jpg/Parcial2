# Cria uma lista vazia para armazenar os nomes
nomes = []

# Loop para solicitar 5 nomes
for i in range(5):
    # Solicita um nome ao usuário
    nome = input("Digite um nome: ")
    
    # Adiciona o nome à lista
    nomes.append(nome)

# Exibe todos os nomes digitados
print("Lista de nomes:")
for nome in nomes:
    print(nome)