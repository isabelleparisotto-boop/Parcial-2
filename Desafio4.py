# Solicite os números ao usuário 
num1 = float(input("Escolha um número "))
num2 = float(input("Escolha outro número "))

#Agora, o usuário deve escolher a operação
operação = input("Escolha uma operação [soma, subtração, divisão ou multiplicação]")

#Vamos realizar as operações 

# Raliza a operação de soma
if operação == "soma":
    print(num1 + num2)
# Realiza a subtração
elif operação == "subtração":
    print(num1-num2)
# Realiza a multiplicação
elif operação == "multiplicação":
    print(num1*num2)
# Realiza a divisão
elif operação == "divisão":
    print(num1/num2)
# Se for uma operaçãop que não existe diga 'esse número não existe'
else:
    print('esse numero não existe')
