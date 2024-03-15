"""
12. Escreva um programa que solicita três números e verifique qual deles é o maior.
"""
# Solicita três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Verifica qual é o maior número
if numero1 >= numero2 and numero1 >= numero3:
    maior_numero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

# Exibe o maior número
print("O maior número é:", maior_numero)
