print('Bem vindo a Lanchonete da Franciele Sousa')

print('****************Cardápio*******************')
print('|Código |       Descrição       |  Valor  |')
print('|  100  |    Cachorro Quente    |   9,00  |')
print('|  101  | Cachorro Quente Duplo |  11,00  |')
print('|  102  |        X-Egg          |  12,00  |')
print('|  103  |        X-Salada       |  13,00  |')
print('|  104  |        X-Bacon        |  14,00  |')
print('|  105  |        X-Tudo         |  17,00  |')
print('|  200  |   Refrigerante Lata   |   5,00  |')
print('|  201  |      Chá Gelado       |   4,00  |')

total = 0     #Define o valor inicial atribuído à variavel

while True:
    codigo = input('Digite o código desejado: ')
    if codigo == '100':
        total += 9     #Guarda o valor dos pedidos
        print('Você pediu um Cachorro Quente no valor de R$ 9,00')
    elif codigo == '101':
        total += 11
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00')
    elif codigo == '102':
        total += 12
        print('Você pediu um X-Egg no valor de R$12,00')
    elif codigo == '103':
        total += 13
        print('Você pediu X-Salada no valor de R$ 13,00')
    elif codigo == '104':
        total += 14
        print('Você pediu um X-Bacon no valor de R$14,00')
    elif codigo == '105':
        total += 17
        print('Você pediu um X-Tudo no valor de R$17,00')
    elif codigo == '200':
        total += 5
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
    elif codigo == '201':
        total += 4
        print('Você pediu um Chá Gelado no valor de R$4,00')
    else:
        print('Opção Inválida!')
        continue
    acrescimo = input('Deseja pedir mais alguma coisa?\n1 - SIM\n0 - Não\n>>')
    if acrescimo == '1':
        continue
    else:
        print('O total a ser pago é R${:.2f}'.format(total))
        break











