nome = 'Jorge Vieira'
altura = 1.65
peso = 45
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Jorge Vieira tem 1.65 de altura,
# pesa 45 quilos e seu IMC é
# 16