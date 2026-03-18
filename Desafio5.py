# Solicita os dados ao usuário
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Realiza o cálculo
area = (base * altura) / 2

# Exibe o resultado com duas casas decimais
print(f"A área do triângulo com base {base} e altura {altura} é: {area:.2f}")
