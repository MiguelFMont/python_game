#Jogo do número secreto
import random

print('''
░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║██║░░██║  ██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██║░░██║  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░

░██████╗███████╗░█████╗░██████╗░███████╗████████╗░█████╗░
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
╚█████╗░█████╗░░██║░░╚═╝██████╔╝█████╗░░░░░██║░░░██║░░██║
░╚═══██╗██╔══╝░░██║░░██╗██╔══██╗██╔══╝░░░░░██║░░░██║░░██║
██████╔╝███████╗╚█████╔╝██║░░██║███████╗░░░██║░░░╚█████╔╝
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝
''')
print('''
V̳o̳c̳ê̳  t̳e̳m̳  1̳0̳  t̳e̳n̳t̳a̳t̳i̳v̳a̳s̳  p̳a̳r̳a̳  a̳c̳e̳r̳t̳a̳r̳  o̳  n̳ú̳m̳e̳r̳o  s̳e̳c̳r̳e̳t̳o̳  e̳n̳t̳r̳e  1̳0̳0̳0̳  e̳  9̳9̳9̳9̳.̳
 A̳  p̳a̳r̳t̳i̳r̳  d̳a̳  5̳º̳  t̳e̳n̳t̳a̳t̳i̳v̳a̳  o̳  j̳o̳g̳o̳  i̳r̳á̳  t̳e̳  a̳j̳u̳d̳a̳r̳,̳  d̳a̳n̳d̳o̳  d̳i̳c̳a̳s̳!̳
''')
input('<<< Tecle Algo Para Continuar! >>>')

numero_secreto = random.randint(1000, 9999)

x = (numero_secreto // 1000)
y = (numero_secreto // 100 - (numero_secreto // 100 - (numero_secreto % 1000))) // 100
z = (numero_secreto // 10) % 10
w = numero_secreto % 10

print(x,y,z,w)

primeiro_digito = '_'
segundo_digito = '_'
terceiro_digito = '_'
quarto_digito = '_'

tentativas = 0

for i in range(1, 10):
    chute = int(input(f'Digite seu chute: '))

    a = (chute // 1000)
    b = (chute // 100 - (chute // 100 - (chute % 1000))) // 100
    c = (chute // 10) % 10
    d = chute % 10
    
    if chute == numero_secreto:
        print(f'Você acertou o número secreto!!\nNúmero de tentativas: {tentativas}')
        print(f'Número secreto: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')
        primeiro_digito = a
        segundo_digito = b
        terceiro_digito = c
        quarto_digito = d
        break
    else:
        if a != x:
            if b!= y:
                if c != z:
                    if d != w:
                        print(f'Você não acertou nenhum digito dessa vez 😓\n\nTente Novamente! Você ainda tem {10 - tentativas} tentativas.\n')
    if a == x:
        primeiro_digito = a
        print(f'Você acertou o primeiro digito (👍 ͡❛ _> ͡❛)👍!')
    if b == y:
        segundo_digito = b
        print(f'Você acertou o segundo digito (👍 ͡❛ _> ͡❛)👍!')
    if c == z:
        terceiro_digito = c
        print(f'Você acertou o terceiro digito (👍 ͡❛ _> ͡❛)👍!')
    if d == w:
        quarto_digito = d
        print(f'Você acertou o quarto digito (👍 ͡❛ _> ͡❛)👍!')
    tentativas += 1

    if tentativas >= 5:
        print(f'Faltam {10-tentativas} tentativas!\n\nVou te dar uma díca!!')
        if a != x:
            if x % 2 == 0:
                print(f'==> O primeiro digito é par!')
                primeiro_digito = 'PAR'
            else:
                print(f'==> O primeiro digito é ímpar!')
                primeiro_digito = 'ÍMPAR'
        elif b!= y:
            if y % 2 == 0:
                print(f'==> O segundo digito é par!')
                segundo_digito = 'PAR'
            else:
                print(f'==> O segundo digito é ímpar!')
                segundo_digito = 'ÍMPAR'
        elif c != z:
            if z % 2 == 0:
                print(f'==> O terceiro digito é par!')
                terceiro_digito = 'PAR'
            else:
                print(f'==> O terceiro digito é ímpar!')
                terceiro_digito = 'ÍMPAR'
        elif d != w:
            if w % 2 == 0:
                print(f'==> O quarto digito é par!')
                quarto_digito = 'PAR'
            else:
                print(f'==> O quarto digito é ímpar!')
                quarto_digito = 'ÍMPAR'

    if tentativas > 10:
        print('Número de tentativas foi exedido!!!')
        
    print(f'Seu código é: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')

