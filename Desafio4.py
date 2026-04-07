# Solicitamos os números ao usuário 
# Através do float que representa números reais e input que é a entrada de dados criamos as variáveis
num1 = float(input("Escolha um número "))
num2 = float(input("Escolha outro número "))

#Agora, o usuário deve escolher a operação
operação = input("Escolha uma operação [soma, subtração, divisão ou multiplicação]")

#Vamos realizar as operações 

# Raliza a operação de soma, através do if que significa 'se'
if operação == "soma":
    print(num1 + num2)
# Realiza a subtração, através do elif que é uma abreviação para 'else if' que significa 'senão se' 
elif operação == "subtração":
    print(num1-num2)
# Realiza a multiplicação, através do elif que é uma abreviação para 'else if' que significa 'senão se' 
elif operação == "multiplicação":
    print(num1*num2)
# Realiza a divisão, através do elif que é uma abreviação para 'else if' que significa 'senão se' 
elif operação == "divisão":
    print(num1/num2)
# Se for uma operação que não existe diga 'esse número não existe' através do 'else' que significa uma variavel caso os comandos sejam contrários aos anteriores
else:
    print('esse numero não existe')
