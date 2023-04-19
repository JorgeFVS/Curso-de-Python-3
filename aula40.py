""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_is_valido = False

    try:
        numero_1_int = int(numero_1)
        numero_2_int = int(numero_2)
        numeros_is_valido = True
    except:
        numeros_is_valido = False

    operadores_permitidos = '+_/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if not numeros_is_valido:
        print('Um ou ambos os numeros digitados são inválidos.')
        continue
    else:
        print("Realizando a sua conta. Confira o resultado abaixo: ")
        if operador == "+":
            print(f'{numero_1_int}+{numero_2_int} =', numero_1_int + numero_2_int)
        elif operador == "-":
            print(f'{numero_1_int}+{numero_2_int} =', numero_1_int - numero_2_int)
        elif operador == "/":
            print(f'{numero_1_int}+{numero_2_int} =', numero_1_int / numero_2_int)
        elif operador == "*":
            print(f'{numero_1_int}+{numero_2_int} =', numero_1_int * numero_2_int)

    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
