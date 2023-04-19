"""
Iterando strings com while
"""
#       012345678910
# nome = 'Jorge Vieira'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

################################################

nome = "Jorge Vieira"
nova_string = ""
indice = 0

while indice < len(nome):

    nova_string += nome[contador]
    adiciona = "*"
    nova_string += adiciona

    indice += 1


print(nova_string)