# Entrada de dados
C = float(input("Digite o capital (C): "))
I = float(input("Digite a taxa de juros (I) em porcentagem: "))
T = float(input("Digite o tempo (T): "))

# Faremos o cálculo dos juros simples
# Aplicando a fórmula: J = (C * I * T) / 100
J = (C * I * T) / 100

# Agora, exibe-se o resultado
print(f"\nCom um capital de R$ {C:.2f}, taxa de {I}% e tempo de {T},")
print(f"o valor dos juros (J) será de: R$ {J:.2f}")
