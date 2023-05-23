print('-------------------------')
print('    CRIANÇA ESPERANÇA    ')
print('-------------------------')
print('Qual opção você deseja escolher? ')
print('[1] Para doar R$ 10,00')
print('[2] Para doar R$ 20,00')
print('[3] Para doar R$ 30,00')
print('[4] Para doar R$ 40,00')
print('[5] Para doar R$ 50,00')
print('[6] Para doar outros valores.')
print('[7] Hoje não. Vou doar em outra oportunidade.')
D = int(input('Opção escolhida: '))
if D == 1:
    print('A sua doação foi de R$ 10,00.\nMuito Obrigado.')
elif D == 2:
    print('A sua doação foi de R$ 20,00.\nMuito Obrigado.')
elif D == 3:
    print('A sua doação foi de R$ 30,00.\nMuito Obrigado.')
elif D == 4:
    print('A sua doação foi de R$ 40,00.\nMuito Obrigado.')
elif D == 5:
    print('A sua doação foi de R$ 50,00.\nMuito Obrigado.')
elif D == 6:
    V = float(input('Qual o valor que deseja doar? R$ '))
    print('A sua doação foi de R$ {:.2f}.\nMuito Obrigado.'.format(V))
else:
    print('Ahhh que pena! Mas tudo bem! Estaremos sempre de braços abertos.')
