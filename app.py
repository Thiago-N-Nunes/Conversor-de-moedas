palavra = 'Macaco'
contador = 1
erro = 0
print('Jogo da Forca')
print('_' * len(palavra))

while erro <= 7:
    tentativa = input('Digite uma letra:')
    if tentativa.lower() in palavra.lower():
        print('ACERTO')
    else:
        print('ERRO')
        erro += 1

    print(f'Numero de Tentativas:{contador}')
    contador +=1
    if erro == 7:
        print('Você perdeu!')
        break