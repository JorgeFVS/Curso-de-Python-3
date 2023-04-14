

#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.


numero_usuario = input("Digite um número inteiro ")

if numero_usuario.isdigit():

    numero_inteiro = int(numero_usuario)

    verifica_par_ou_impar = numero_inteiro % 2 == 0

    if verifica_par_ou_impar:
        print("O número digitado é par")
    elif verifica_par_ou_impar:
        print("O número digitado é impar")

else:
    print("Você não digitou um numero inteiro!")


#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

horas_usuario = input("Digite que horas são ")

if horas_usuario.isdigit():

    horas_usuario_int = int(horas_usuario)

    if horas_usuario_int <= 11:
        print("Bom dia")
    elif horas_usuario_int > 11 and horas_usuario_int <= 17:
        print("Boa tarde")
    else:
        print("Boa noite")
else:
    print("Você não digitou um numero inteiro!")    


#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

