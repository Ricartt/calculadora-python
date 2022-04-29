# soma
def soma(x, y):
    return x + y
# subtração


def sub(x, y):
    return x - y
# multiplicação


def mult(x, y):
    return x * y
# divisão


def div(x,  y):
    return x / y


print('------------Calculadora----------')
opcoes = input(
    '\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\nDigite o número da operação que deseja fazer: ')

while opcoes >= '5':
    print('Opção invalida\n')
    opcoes = input(
        'Opçoes: \n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\nDigite o número da operação que deseja fazer: ')

if opcoes == '1':
    num = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('\n', num, '+', num2, '=', soma(num, num2))

elif opcoes == '2':
    num = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('\n', num, '-', num2, '=', sub(num, num2))

elif opcoes == '3':
    num = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('\n', num, '*', num2, '=', mult(num, num2))

elif opcoes == '4':
    num = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('\n', num, '/', num2, '=', div(num, num2))
