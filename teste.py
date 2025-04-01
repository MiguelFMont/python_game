#Jogo do número secreto
import random
x = 0
while x != 1:
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

    # print(numero_secreto)

    primeiro_digito = '_'
    segundo_digito = '_'
    terceiro_digito = '_'
    quarto_digito = '_'

    tentativas = 0
    dica_par_impar = 1
    dica_maior_menor = 0
    digitos_certos = 0
    digitos_errados = 0

    while tentativas < 10:
        
        chute = int(input(f'\nDigite seu chute: '))

        if chute < 1000: 
            print('Número inválido! Digite somente números entre 1000 a 9999')

        elif chute > 9999:
            print('número inválido! Digite somente números entre 1000 a 9999')

        else:
            a = (chute // 1000)
            b = (chute // 100 - (chute // 100 - (chute % 1000))) // 100
            c = (chute // 10) % 10
            d = chute % 10

            if primeiro_digito != x:
                if a == x:
                    primeiro_digito = x
                    print(f'\nVocê acertou o primeiro dígito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1
                    
            if segundo_digito != y:
                if b == y:
                    segundo_digito = y
                    print(f'\nVocê acertou o segundo digito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1

            if terceiro_digito != z:
                if c == z:
                    terceiro_digito = z
                    print(f'\nVocê acertou o terceiro dígito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1

            if quarto_digito != w:      
                if d == w:
                    quarto_digito = w
                    print(f'\nVocê acertou o quarto dígito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1
                    
            if chute == numero_secreto:
                print(f'\nVocê acertou o número secreto!!\nNúmero de tentativas: {tentativas}\n')
                print(f'Número secreto: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')
                break
            
            if tentativas == 10:
                print(f'Você não conseguiu acertar!!\nO número secreto era: {numero_secreto}')
                break

            if digitos_certos == 0:
                print('\nVocê não acertou nenhum dígito dessa vez...')

            digitos_certos = 0
            print(f'\nfaltam {9-tentativas} tentativas...') 

            if tentativas >= 5:
                print(f'\nVou te dar uma dica!!')
                if dica_maior_menor == 1:
                    if primeiro_digito != x:
                        if a > x:
                                print(f'==> O primeiro dígito é menor que {a}')
                                primeiro_digito = f'<{a}'
                        else: 
                                print(f'==> O primeiro dígito é maior que {a}')
                                primeiro_digito = f'>{a}'
                    elif segundo_digito != y:
                        if b > y:
                                print(f'==> O segundo dígito é menor que {b}')
                                segundo_digito = f'<{b}'
                        else:
                                print(f'==> O segundo dígito é maior que {b}')
                                segundo_digito = f'>{b}'
                    elif terceiro_digito != z:           
                        if c > z:
                                print(f'==> O terceiro dígito é menor que {c}')
                                terceiro_digito = f'<{c}'
                        else:
                                print(f'==> O terceiro dígito é maior que {c}')
                                terceiro_digito = f'>{c}'
                    elif quarto_digito != w:           
                        if d > w:
                                print(f'==> O quarto dígito é menor que {d}')
                                quarto_digito = f'<{d}'
                        else:
                                print(f'==> O quarto dígito é maior que {d}')
                                quarto_digito = f'>{d}'
                    
                if dica_par_impar == 1:
                    if a != x:
                        if x % 2 == 0:
                            print(f'==> O primeiro dígito é par!')
                            primeiro_digito = 'PAR'
                        else:
                            print(f'==> O primeiro dígito é ímpar!')
                            primeiro_digito = 'ÍMPAR'
                    elif b!= y:
                        if y % 2 == 0:
                            if y == 0:
                                if b > y:
                                    print(f'==> O segundo dígito é menor que {a}')
                                    segundo_digito = f'<{a}'
                                else: 
                                    print(f'==> O segundo dígito é maior que {a}')
                                    segundo_digito = f'>{a}'
                            else:
                                print(f'==> O segundo dígito é par!')
                                segundo_digito = 'PAR'
                        else:
                            print(f'==> O segundo dígito é ímpar!')
                            segundo_digito = 'ÍMPAR'
                    elif c != z:
                        if z % 2 == 0:
                            if z == 0:
                                if c > z:
                                    print(f'==> O terceiro dígito é menor que {c}')
                                    terceiro_digito = f'<{c}'
                                else:
                                    print(f'==> O terceiro dígito é maior que {c}')
                                    terceiro_digito = f'>{c}'
                            else:
                                print(f'==> O terceiro dígito é par!')
                                terceiro_digito = 'PAR'
                        else:
                            print(f'==> O terceiro dígito é ímpar!')
                            terceiro_digito = 'ÍMPAR'
                    elif d != w:
                        if w % 2 == 0:
                            if w == 0:
                                if d > w:
                                    print(f'==> O quarto dígito é menor que {d}')
                                    quarto_digito = f'<{d}'
                                else:
                                    print(f'==> O quarto dígito é maior que {d}')
                                    quarto_digito = f'>{d}'
                            else:
                                print(f'==> O quarto dígito é par!')
                                quarto_digito = 'PAR'
                        else:
                            print(f'==> O quarto dígito é ímpar!')
                            quarto_digito = 'ÍMPAR'
                    dica_par_impar -= 1
                    dica_maior_menor += 1
                    
            tentativas += 1
            print(f'\nSeu código é: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}') 

    continuar_parar = int(input('\nDeseja continuar o jogo? 1 = SIM || 0 = NÃO: '))
    if continuar_parar == 1:
        x = 0
    else: 
        x = 1