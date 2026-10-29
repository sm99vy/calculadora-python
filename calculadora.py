from time import sleep

cor = {
    'nverde': '\033[1;32m',
    'samarelo': '\033[4;33m',
    'nsvermelho': '\033[1;4;31m',
    'sazul': '\033[4;34m',
    'nsfazul': '\033[1;4;37;44m',
    'nsfpreto': '\033[1;4;37;40m',
    'r': '\033[m'
}

print(f'{cor["nsfpreto"]}═'*40)
print(f'{cor["nsfpreto"]}═{cor["r"]}'*14 + f'{cor["nsfazul"]}CALCULADORA{cor["r"]}' + f'{cor["nsfpreto"]}═{cor["r"]}'*15)
print(f'{cor["nsfpreto"]}═{cor["r"]}'*40)
sleep(1)

while True:
    try:
        n1 = float(input(f'{cor["sazul"]}Digite o primeiro número: ').replace(',', '.'))
        sleep(0.4)
        operation = input(f'{cor["samarelo"]}Agora me diga qual operação deseja (+, -, *, /): ').strip()
        sleep(0.4)
        n2 = float(input(f'\n{cor["sazul"]}Certo. Agora, me diga o segundo número: ').replace(',', '.'))
        sleep(0.4)
        
        print(f'\nGerando resultado...{cor["r"]}\n')
        sleep(0.5)

        if operation == '+':
            result = n1 + n2
            print(f'{cor["nverde"]}O resultado de {n1:g} + {n2:g} equivale a {result:g}!{cor["r"]}')
        elif operation == '-':
            result = n1 - n2
            print(f'{cor["nverde"]}O resultado de {n1:g} - {n2:g} equivale a {result:g}!{cor["r"]}')
        elif operation == '*':
            result = n1 * n2
            print(f'{cor["nverde"]}O resultado de {n1:g} * {n2:g} equivale a {result:g}!{cor["r"]}')
        elif operation == '/':
            if n2 == 0:
                print(f'{cor["nsvermelho"]}Erro: Não dá para dividir por 0!{cor["r"]}')
            else:
                result = n1 / n2
                print(f'{cor["nverde"]}O resultado de {n1:g} / {n2:g} equivale a {result:g}!{cor["r"]}')
        else:
            print(f'{cor["nsvermelho"]}Operação inválida!{cor["r"]}')
    except ValueError:
        print(f'{cor["nsvermelho"]}Entrada inválida! Digite números válidos.{cor["r"]}')

    continuar = input(f'{cor["samarelo"]}Deseja fazer outro cálculo? (S/N): ').strip().upper()
    print(f'{cor["r"]}')
    while continuar not in 'SN':
        continuar = input(f'{cor["nsvermelho"]}Erro: Digite "S" para SIM e "N" para NÃO continuar!: ').strip().upper()
        print(f'{cor["r"]}')
    if continuar == 'N':
        sleep(0.3)
        print(f'{cor["nverde"]}Encerrando...')
        sleep(0.2)

        print(f'Calculadora encerrada. Até mais!{cor["r"]}')
        break
