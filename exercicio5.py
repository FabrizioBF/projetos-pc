# Solicita ao usuário para digitar o peso em kg e a altura em metros
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC usando a fórmula IMC = peso / altura²
imc = peso / (altura ** 2)

# Exibe o resultado do IMC
print("Seu Índice de Massa Corporal (IMC) é:", imc)
