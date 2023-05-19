H = float(input('Altura: '))
S = input('Sexo: ')
P = 0
if S == 'm':
    P = 72.7*H-58
    print('Seu peso ideal é: ',P)
elif S == 'f':
    P = 62.1*H-44.7
    print('Seu peso ideal é: ',P)
else:
    print('Inválido')