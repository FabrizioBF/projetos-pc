# Solicita ao usuário para digitar a largura e o comprimento do retângulo
largura = float(input("Digite a largura do retângulo: "))
comprimento = float(input("Digite o comprimento do retângulo: "))

# Calcula o perímetro do retângulo usando a fórmula P = 2(l + c)
perimetro = 2 * (largura + comprimento)

# Calcula a área do retângulo usando a fórmula A = l * c
area = largura * comprimento

# Exibe o resultado do perímetro e da área do retângulo
print("O perímetro do retângulo é:", perimetro)
print("A área do retângulo é:", area)
