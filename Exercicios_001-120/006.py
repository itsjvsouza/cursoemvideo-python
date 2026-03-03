#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))
n2 = n*2
n3 = n*3
nr = n**(1/2)

print('O dobro, triplo e a raiz de {} são respectivamente {}, {} e {}'.format(n, n2, n3, nr))
