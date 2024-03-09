# Importa o módulo math para utilizar a constante pi
import math

# Solicita ao usuário o valor do raio da esfera
raio = float(input("Digite o valor do raio da esfera: "))

# Calcula o volume da esfera utilizando a fórmula V = (4/3) * pi * raio³
volume = (4/3) * math.pi * raio**3

# Exibe o resultado do volume da esfera
print("O volume da esfera é:", volume)
