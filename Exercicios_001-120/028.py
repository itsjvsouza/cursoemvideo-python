#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)

num_user = int(input('Tente acertar qual número escolhi entre 0 e 5: '))

if num_user == num:
    print('Você acertou o número!')

else:
    print('Você errou o número kkkkkkkkkkkkkkkkkkkkk')
