num = int(input("Digite um número inteiro: "))
primo = True

for i in range(2, num):
    if num % i == 0:
        print(f"\nO número {num} não é primo.")
        primo = False
        break

if primo == True:
    print(f"\nO número {num} é primo.")
