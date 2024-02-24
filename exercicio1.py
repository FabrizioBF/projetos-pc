# Solicita ao usuário para digitar os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a soma dos números
soma = numero1 + numero2
print("A soma dos números é:", soma)

# Calcula a subtração dos números
subtracao = numero1 - numero2
print("A subtração dos números é:", subtracao)

# Calcula a multiplicação dos números
multiplicacao = numero1 * numero2
print("A multiplicação dos números é:", multiplicacao)

# Calcula a divisão dos números (verifica se o segundo número é diferente de zero)
if numero2 != 0:
    divisao = numero1 / numero2
    print("A divisão dos números é:", divisao)
else:
    print("Não é possível dividir por zero.")
