# Entrada do usuário
total_segundos = int(input("Digite a quantidade de segundos: "))

#Faz-se o cálculo das horas (divisão inteira por 3600)
horas = total_segundos // 3600

# Aquilo que sobrar das horas, usamos para calcular os minutos
resto_segundos = total_segundos % 3600
minutos = resto_segundos // 60

# Aquilo que sobrar dos minutos são os segundos finais
segundos_finais = resto_segundos % 60

print(f"{total_segundos} segundos equivalem a:")
print(f"{horas}h {minutos}min {segundos_finais}s")
