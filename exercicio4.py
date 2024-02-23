import math

# Solicita ao usuário para digitar os três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Calcula a média geométrica dos números
media_geometrica = math.pow(numero1 * numero2 * numero3, 1/3)

# Exibe o resultado da média geométrica
print("A média geométrica dos números é:", media_geometrica)
