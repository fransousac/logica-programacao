print('Bem vindo à Companhia de Logística Franciele da Cruz Sousa')

def dimensoesObjeto():
    while True:
        try:
            #Pegar as dimensões do objeto
           alt = float(input('Informe a altura do objeto (cm): '))
           larg = float(input('Informe a largura do objeto (cm): '))
           comp = float(input('Informe o comprimento do objeto (cm): '))
           volume = alt * larg * comp
           print('O volume do objeto é {} cm³'.format(volume))

        #Tarifa de acordo com o volume
           if volume < 1000:
              return 10
           elif 1000 <= volume < 10000:
              return 20
           elif 10000 <= volume < 30000:
              return 30
           elif 30000 <= volume < 100000:
              return 50
           else:
                print('Não aceitamos objetos com dimensões tão grandes')
                print('Digite novamente as dimensões desejadas')
        except ValueError:
            print('Você digitou alguma dimensão com valor não numérico')
            print('Digite as dimensões desejadas novamente, por favor')

def pesoObjeto():
    while True:
        try:
            #Calcula o peso do objeto e direciona para a tarifa
            peso = float(input('Informe o peso do objeto (kg): '))

            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados!')
                print('Por favor, digite o peso desejado novamente')
        except ValueError:
            print("Você digitou o peso do objeto com valor não numérico")
            print("Por favor, digite o peso desejado novamente")

def rotaObjeto():
    while True:
            #Função que direciona as rotas para o valor da tarifa
            rota = (input('Selecione a rota: \nFG - De Florianópolis para Gramado\nFS - De Florianópolis para São Paulo\nGF - De Gramado para Florianópolis\nGS - De Gramado para São Paulo\nSG - De São Paulo para Gramado\nSF - São Paulo para Florianópolis\n'))
            if rota == 'FG':
                return 1
            elif rota == 'FS':
                return 1
            elif rota == 'GF':
                return 1.2
            elif rota == 'GS':
                return 1.2
            elif rota == 'SG':
                return 1.5
            elif rota == 'SF':
                return 1.5
            else:
                print('Você digitou uma rota inexistente!')
                print('Por favor ,digite a rota desejada novamente')

dim = dimensoesObjeto()
peso = pesoObjeto()
trajeto = rotaObjeto()
total = dim * peso * trajeto
print('O valor total a ser pago é R${:.2f}\n(Dimensões: {} * Peso: {} * Rota: {}'.format(total, dim, peso, trajeto))













