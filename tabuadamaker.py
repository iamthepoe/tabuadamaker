import os
import time
res = 'S'
while(res == 'S') | (res == 's'):
    print('===========================')
    print('TABUADA MAKER')
    print('===========================')
    cont = 1
    num = int(input('Digite o número desejado: '))
    tabnum = int(input('Digite quantas vezes ele irá ser multiplicado: '))

    while(cont<=tabnum):
        print(f'{num} x {cont} = {num * cont}')
        cont = cont + 1

    print('Deseja escolher novamente? [S/N]')
    res = str(input(''))
    os.system('cls') or None
