print('Bem vindo à loja da Franciele da Cruz Sousa ')
p = float(input('Qual é o valor do produto? R$'))
qtd = float(input('Qual a quantidade? '))
total = p * qtd
if (qtd <= 9):
     #O produto não tem desconto
    print('o valor com 0% de desconto foi de {:.2f}'.format(total))
elif (10 <= qtd <= 99):
     # Calculo de 5 % de desconto
     desc = total - (total * 5 / 100)
     print('O valor sem desconto foi de {:.2f}'.format(total))
     print('O valor com 5% de desconto foi de {:.2f}'.format(desc))
elif (100 <= qtd <= 999):
     # Calculo de 10 % de desconto
     desc = total - (total * 10 / 100)
     print('O valor sem desconto foi de R$ {:.2f}'.format(total))
     print('O valor com 10% de desconto foi de R$ {:.2f}'.format(desc))
else:
     desc = total - (total * 15 / 100)
     # Calculo de 15 % de desconto
     print('O valor sem desconto foi de {:.2f}'.format(total))
     print('O valor com 15% de desconto foi de {:.2f}'.format(desc))











