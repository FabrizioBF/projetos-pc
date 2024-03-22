"""
25.Escreva um programa que leia a idade do usuário e apresente uma mensagem, informando se o usuário é uma criança,
adolescente, adulto ou idoso.
"""

idade = int(input("Digite a idade: "))

if idade <= 12:
	print("Criança")
elif idade <= 17:
	print("Adolescente")
elif idade <= 59:
	print("Adulto")
else:
	print("Idoso")
