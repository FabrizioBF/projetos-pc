# Solicita ao usuário para digitar a massa do objeto e a velocidade
massa = float(input("Digite a massa do objeto (m): "))
velocidade = float(input("Digite a velocidade do objeto (v): "))

# Calcula a energia cinética usando a fórmula E = (mv²) / 2
energia_cinetica = (massa * velocidade ** 2) / 2

# Exibe o resultado da energia cinética
print("A energia cinética do objeto é:", energia_cinetica)
