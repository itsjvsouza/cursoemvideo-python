#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Qual sua primeira anota? '))
n2 = float(input('Qual sua segunda anota? '))
media = (n1 + n2) / 2

print('Sua média entre {} e {} foi {:.2f}'.format(n1, n2, media))
