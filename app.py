import os

print('=' * 30)
print('CONVERSOR DE MOEDAS')
print('=' * 30)
valor = float(input('Digite um valor: '))
os.system('cls')
print('=' * 30)
print('CONVERSÃO')
print('=' * 30)
escolha = int(input(f'\n Qual moeda você deseja converter o valor de R$ {valor:.2f}?\n1. Dolar\n2. Euro\n3. Libra\n4. Ienes\n'))
match escolha:
    case 1:
        print(f'O valor de R${valor:.2f} convertido para U${(valor / 4.95):.2f}')
    case 2:
        print(f'O valor de R${valor:.2f} convertido para \u20AC{(valor / 5.85):.2f}')
    case 3:
        print(f'O valor de R${valor:.2f} convertido para \u00A3{(valor / 6.73):.2f}')
    case 4:
         print(f'O valor de R${valor:.2f} convertido para \u00A5{(valor / 0.032):.2f}')