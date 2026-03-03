#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))
an = n - 1
sa = n + 1

print('O sucessor de {} é {} e o antecessor é {}'.format(n, sa, an))
