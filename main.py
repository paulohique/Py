def welcome():
    print('''Seja bem vindo a calculadora do PH''')
    
def calculate():
    operation = input('''
Por favor selecione a operação:
                  + adição
                  - subtração
                  * multiplicação
                  / divisao
                  ''')

    number_1 = int(input('Coloque o primeiro numero!'))
    number_2 = int(input('Coloque o segundo numero!'))
    if operation == '+':
        print('{} + {} ='.format(number_1,number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} ='.format(number_1,number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} ='.format(number_1,number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} ='.format(number_1,number_2))
        print(number_1 / number_2)
    else:
        print('Seu resultado não pode ser obtido')

 # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Quer calcular denovo? S para sim ou N para não
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()
welcome()
calculate()
