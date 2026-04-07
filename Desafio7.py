# Entrada de dados
# Criamos as variáveis 'C' para capital, 'J' para juros e 'T' para tempo. através de float para números reais e input para entrada de dados 
C = float(input("Digite o capital : "))
I = float(input("Digite a taxa de juros: "))
T = float(input("Digite o tempo : "))

# Faremos o cálculo dos juros simples
# Aplicando a fórmula: J = (C * I * T) / 100
J = (C * I * T) / 100

# Agora, exibe-se o resultado através de 'print' que é saída de dados
print("O valor do juros é:") 
print(J)
