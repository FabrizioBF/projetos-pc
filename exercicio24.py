""""
24.Escreva um programa que peça a altura (ex. 1.78) e o peso (80.5) do usuário e em seguida calcule o imc, informando também
 se está abaixo do peso, se está com peso normal, se está com sobrepeso, se está com obesidade ou se está com obesidade grave.
"""

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

imc = peso / (altura ** 2)

if imc < 18.5:
	categoria = "abaixo do peso"
elif imc < 25:
	categoria = "peso normal"
elif imc < 30:
	categoria = "sobrepeso"
elif imc < 35:
	categoria = "obesidade"
else:
	categoria = "obesidade grave"

print(f"Seu IMC é: {imc:.2f}")
print(f"Categoria: {categoria}")
