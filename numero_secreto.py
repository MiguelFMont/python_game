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
dica_par_impar = 1
dica_maior_menor = 0

for i in range(1, 11):
    chute = int(input(f'\nDigite seu chute: '))

    if chute < 1000: 
        print("Número inválido! Digite somente números entre 1000 a 9999")
    elif chute > 9999:
        print("número inválido! Digite somente números entre 1000 a 9999")
    else:
        tentativas += 1

        a = (chute // 1000)
        b = (chute // 100 - (chute // 100 - (chute % 1000))) // 100
        c = (chute // 10) % 10
        d = chute % 10
        
        print(f'\nfaltam {10-tentativas} tentativas...')    

        if tentativas >= 2:
            print(f'\nVou te dar uma díca!!')
            if dica_maior_menor == 1:
                if a != x:
                    if a > x:
                            print(f'==> O primeiro digito é menor que {a}')
                            primeiro_digito = f'<{a}'
                    else: 
                            print(f'==> O primeiro digito é maior que {a}')
                            primeiro_digito = f'>{a}'
                elif b != y:
                    if b > y:
                            print(f'==> O segundo digito é menor que {b}')
                            segundo_digito = f'<{b}'
                    else:
                            print(f'==> O segundo digito é maior que {b}')
                            segundo_digito = f'>{b}'
                elif c != z:           
                    if c > z:
                            print(f'==> O terceiro digito é menor que {c}')
                            terceiro_digito = f'<{c}'
                    else:
                            print(f'==> O terceiro digito é maior que {c}')
                            terceiro_digito = f'>{c}'
                elif d != w:           
                    if d > w:
                            print(f'==> O quarto digito é menor que {d}')
                            quarto_digito = f'<{d}'
                    else:
                            print(f'==> O quarto digito é maior que {d}')
                            quarto_digito = f'>{d}'
                
            if dica_par_impar >= 1:
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
                dica_par_impar -= 1
                dica_maior_menor += 1

        if primeiro_digito != a:
            if a == x:
                primeiro_digito = a
                print(f'Você acertou o primeiro digito (👍 ͡❛ _> ͡❛)👍!')

        if segundo_digito != b:
            if b == y:
                segundo_digito = b
                print(f'Você acertou o segundo digito (👍 ͡❛ _> ͡❛)👍!')
        if terceiro_digito != c:
            if c == z:
                terceiro_digito = c
                print(f'Você acertou o terceiro digito (👍 ͡❛ _> ͡❛)👍!')

        if quarto_digito != d:      
            if d == w:
                quarto_digito = d
                print(f'Você acertou o quarto digito (👍 ͡❛ _> ͡❛)👍!\n')

        if tentativas == 10:
            print(f'Você não conseguiu acertar!!\nO número secreto era: {numero_secreto}')
            break

        if chute == numero_secreto:
            print(f'Você acertou o número secreto!!\nNúmero de tentativas: {tentativas}\n')
            print(f'Número secreto: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')
            break
        else:
            if a != x:       
                if b!= y:
                    if c != z:
                        if d != w:
                            print(f'Você não acertou nenhum digito dessa vez 😓\n\nTente Novamente!')

        print(f'\nSeu código é: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')  