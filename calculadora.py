# Calculadora simples em Python

while True:
    try:
        n1 = float(input('\033[4;34mDigite o primeiro número: \033[m').replace(',', '.'))
        op = input('\033[4;33mAgora me diga qual operação deseja (+, -, *, /): \033[m').strip()
        n2 = float(input('\033[4;34mDigite o segundo número: \033[m').replace(',', '.'))

        if op == '+':
            res = n1 + n2
            print(f'\033[1;32mO resultado de {n1:g} + {n2:g} equivale a {res:g}!\033[m')
        elif op == '-':
            res = n1 - n2
            print(f'\033[1;32mO resultado de {n1:g} - {n2:g} equivale a {res:g}!\033[m')
        elif op == '*':
            res = n1 * n2
            print(f'\033[1;32mO resultado de {n1:g} * {n2:g} equivale a {res:g}!\033[m')
        elif op == '/':
            if n2 == 0:
                print('\033[1;4;31mErro! Não dá para dividir por 0!\033[m')
            else:
                res = n1 / n2
                print(f'\033[1;32mO resultado de {n1:g} / {n2:g} equivale a {res:g}!\033[m')
        else:
            print('\033[1;4;31mOperação inválida!\033[m')

    except ValueError:
        print('\033[1;4;31mEntrada inválida! Digite números válidos.\033[m')

    continuar = input('\033[4;33mDeseja fazer outro cálculo? (s/n): \033[m').strip().lower()
    if continuar != 's':
        print('\033[1;32mCalculadora encerrada. Até mais!\033[m')
        break
