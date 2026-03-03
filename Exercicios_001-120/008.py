#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))
c =  m * 100
mili = m * 1000

print('{} metro(s) = {}centímetro(s) = {} milímetro(s)'.format(m, c, mili))