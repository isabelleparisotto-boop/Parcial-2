# Primeiro, solicite os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Depois, solicite a escolha da operação
print("\nEscolha a operação:")
print("+ : Soma")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")
operacao = input("Digite o símbolo da operação: ")

# Por último, realize o cálculo baseado na escolha
if operacao == "+":
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")

elif operacao == "/":
    # Por último, verifique para evitar erro de divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero!")

else:
    print("\nOperação inválida. Tente novamente.")
