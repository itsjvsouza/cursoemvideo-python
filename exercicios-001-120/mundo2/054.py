qnt_maior_idade = 0
qnt_menor_idade = 0

for i in range(7):
    ano = int(input(f"Digite o ano de nascimento da {i + 1}° pessoa: "))
    if ano <= 2007:
        qnt_maior_idade += 1
    else:
        qnt_menor_idade += 1

print(f"\n{qnt_maior_idade} pessoas tem mais de 18 anos.")
print(f"{qnt_menor_idade} pessoas tem menos de 18 anos.")
