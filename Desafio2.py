# Perguntamos ao usuário que digite um número
# Fazemos a pergunta 
# Através de int que é para números inteiros e o input que é para entrada de dados
numero = int(input("Digite um número: "))

# Verificamos se o número é par
# O if e o else são para e se o número for divisível por 2 ele é par, se não ele é ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

