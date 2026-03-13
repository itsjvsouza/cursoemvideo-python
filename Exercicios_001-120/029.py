#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade do carro? '))

if v > 80:
    print('\nVocê foi multado!')
    print(f'\nVocê pagará R${(v - 80) * 7} de multa.')

else:
    print('Você está dentro do limite de velocidade!')
