PG = 1.80; PA = 1.0; VG = 0.0
TC = input('Tipo de carro: ')
CT = float(input('Capacidade do tanque: '))
if TC == 'G':
    VG = CT*PG
    print('Valor gasto: R$',VG)
elif TC == 'A':
    VG = CT*PA
    print('Valor gasto: R$',VG)
else:
    print('Inválido')