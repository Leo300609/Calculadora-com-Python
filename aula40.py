# Calculadora com while

while True:
    num1 = input('Me diga o primeiro número: ')
    num2 = input('Me diga o segundo número: ')
    operador = input('Me diga qual é o operador(+ - * /): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = True

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadors_permitidos = "+-*/"

    if operador not in operadors_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)


    sair = input('Quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break