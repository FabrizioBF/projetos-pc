"""
11. Escreva um programa para verificar se o primeiro número ou o segundo número é maior, caso
 contrário eles são iguais.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")
