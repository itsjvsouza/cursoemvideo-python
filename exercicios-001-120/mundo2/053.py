palavra = input("Digite uma palavra: ").strip().lower()
palavra2 = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra2 += palavra[i]

if palavra == palavra2:
    print(f"\nA palavra {palavra} é um palíndromo.")
else:
    print(f"\nA palavra {palavra} não é um palíndromo.")
