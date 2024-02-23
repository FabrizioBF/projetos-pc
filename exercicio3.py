
# Solicita ao usuário para digitar as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado da média aritmética
print("A média aritmética das notas é:", media)

# Solicita ao usuário para digitar as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética das notas
media = (nota1 + nota2 + nota3) / 3

# Formata o resultado para exibir duas casas decimais
media_formatada = "{:.2f}".format(media)

# Exibe o resultado da média aritmética com duas casas decimais
print("A média aritmética das notas é:", media_formatada)
