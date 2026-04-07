# Usuário vai escrever a quantidade de segundos 
# Criamos a variável dos segundos, atraves d int que é para números inteiros e o input que é para entrada de dados 
seg = int(input("Digite a quantidade de segundos: "))

# Aqui são os cálculos 
# Haverá a divisão dos segundos por 3600 para descobrir as horas 
horas = seg // 3600 
# Para saber os  minutos, dividimos os segundos por 60
min = seg // 60 
# Aqui terá a resposta através do 'print' que é para saída de dados  
print("minutos")
print(min)
print("horas")
print(horas)

# O programa calculará a quantidade de minutos e segundos através das horas através do int que é para números inteiros e o input que é para entrada de dados 
horas1 = int(input("Digite a quantidade de horas: "))
# Aqui são os cálculos
# Assim, multiplicamos as horas por 60 para saber os minutos
min1 = horas1 * 60 
# E multiplicamos as horas por 3600 para saber os segundos 
seg1 = horas * 3600
# Aqui terá a resposta através do 'print' que é para saída de dados  
print("minutos")
print(min1)
print("segundos")
print(seg1)
