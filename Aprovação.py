faltas = int(input('Digite a quantidade de faltas do aluno: '))

if faltas >= 15:
    print('Reprovado por faltas.')

else:
    AV1 = float(input('Nota da AV1: '))
    AV2 = float(input('Nota da AV2: '))
    media = (AV1+AV2)/2

    if media >= 7:
        print('aprovado por média.')

    elif media < 3:
        print('Reprovado por média.')

    else:
        print('Prova final.')