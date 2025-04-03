#Jogo do número secreto
import random
import os
import time
condicao_jogar_novamente_ou_parar = '0'
while condicao_jogar_novamente_ou_parar != '1':

    iniciar = 0

    while iniciar == 0:
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
        print('V̳o̳c̳ê̳  t̳e̳m̳  1̳0̳  t̳e̳n̳t̳a̳t̳i̳v̳a̳s̳  p̳a̳r̳a̳  a̳c̳e̳r̳t̳a̳r̳  o̳  n̳ú̳m̳e̳r̳o  s̳e̳c̳r̳e̳t̳o̳  e̳n̳t̳r̳e  1̳0̳0̳0̳  e̳  9̳9̳9̳9̳.̳')
        jogar_regras = (input('<<< Tecle 1 Para Jogar! | Tecle 2 Para Exibir as Regras! >>>\n '))
        
        if jogar_regras == '1':
            break
        elif jogar_regras == '2':
            print('''
            █▀█ █▀▀ █▀▀ █▀█ ▄▀█ █▀   █▀▄ █▀█   ░░█ █▀█ █▀▀ █▀█ ▀
            █▀▄ ██▄ █▄█ █▀▄ █▀█ ▄█   █▄▀ █▄█   █▄█ █▄█ █▄█ █▄█ ▄
            
            • Objetivo: 
                Acertar o número secreto, que é um número entre 1000 e 9999.
            
            • Tentativas: 
                Você tem 10 tentativas para adivinhar o número secreto.
            
            • Validação: 
                Se você inserir um valor inválido (como uma letras, espaços ou não digitar um número entre 1000 a 9999), será solicitado que tente novamente.
                A partir da terceira vez que um valor inválido for digitado, o jogo começará a descontar tentativas.
            
            • Chutes: 
                Após passar da validação, o sistema irá informar:
                - Se você acertou algum dígito (e quais foram).
                - Se não acertou nenhum.
                Todos os dígitos descobertos ficarão salvos e serão mostrados durante todo o jogo.
            
            • Dicas:
                A partir da 5ª tentativa, você recebe dicas sobre os dígitos:
                - Primeira Dica => Ínforma se o dígito secreto é par ou ímpar.
                - Segunda Dica => Ínforma se o dígito secreto é maior ou menor que o seu chute.
                A segunda dica só é ínformada caso o usuário não tenha acertado o dígito secreto após a primeira dica (Par ou ímpar)

            • Fim do Jogo:
                O jogo termina se:
                - Você acertar o número secreto.
                - Você fazer 10 tentativas sem acertar.
            
            • Reiniciar:
                Após o fim de uma rodada, você pode escolher continuar ou sair.

                ''')
            input('<<< Tecle enter para retornar >>>')
            os.system('cls')
        else:
            if jogar_regras != '1' or jogar_regras != '2' or jogar_regras == '':
                os.system('cls')
                print('<<< Digite somente 1 ou 2! >>>')
            
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

    validacao_de_entrada = 0
    cont_validacao_errada = 0
    cont = 0

    while cont < 10:
        
        while validacao_de_entrada == 0:

            print(f'\nDigitos descobertos são: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')
            chute = (input(f'\nDigite seu chute: '))
            if chute == '':
                os.system('cls')
                time.sleep(0.2)
                print('Entrada inválida. Digite apenas números.')
                cont_validacao_errada += 1
                if cont_validacao_errada >= 3:
                    tentativas += 1
                    time.sleep(0.2)
                    print(f'Faltam {10-tentativas} tentativa(s)...')
            else:
                for digitos in chute:
                    if digitos < '0' or digitos > '9':
                        os.system('cls')
                        time.sleep(0.2)
                        print('Entrada inválida. Digite apenas números.')
                        cont_validacao_errada += 1
                        if cont_validacao_errada >= 3:
                            tentativas += 1
                            time.sleep(0.2)
                            print(f'Faltam {10-tentativas} tentativa(s)...')
                        break
                else:
                    chute = int(chute)
                    if chute < 1000 or chute > 9999:
                        os.system('cls')
                        time.sleep(0.2)
                        print('número inválido! Digite somente números entre 1000 a 9999')
                        cont_validacao_errada += 1
                        if cont_validacao_errada >= 3:
                            tentativas += 1
                            time.sleep(0.2)
                            print(f'Faltam {10-tentativas} tentativa(s)...')
                    else:
                        tentativas += 1
                        break

            if tentativas == 10:
                break 
        if tentativas == 10:
                print(f'Você não conseguiu acertar!!\nO número secreto era: {numero_secreto}')
                break
        if tentativas < 10:
            a = (chute // 1000)
            b = (chute // 100 - (chute // 100 - (chute % 1000))) // 100
            c = (chute // 10) % 10
            d = chute % 10

            if primeiro_digito != x:
                if a == x:
                    primeiro_digito = x
                    time.sleep(0.2)
                    print(f'\nVocê acertou o primeiro dígito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1
                        
            if segundo_digito != y:
                if b == y:
                    segundo_digito = y
                    time.sleep(0.2)
                    print(f'\nVocê acertou o segundo digito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1

            if terceiro_digito != z:
                if c == z:
                    terceiro_digito = z
                    time.sleep(0.2)
                    print(f'\nVocê acertou o terceiro dígito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1

            if quarto_digito != w:      
                if d == w:
                    quarto_digito = w
                    time.sleep(0.2)
                    print(f'\nVocê acertou o quarto dígito (👍 ͡❛ _> ͡❛)👍!')
                    dica_maior_menor = 0
                    dica_par_impar = 1
                    digitos_certos = 1

            if primeiro_digito == x:
                if segundo_digito == y:
                    if terceiro_digito == z:
                        if quarto_digito == w:
                            time.sleep(0.2)
                            print(f'\nVocê acertou o número secreto!!\nNúmero de tentativas: {tentativas}\n')
                            time.sleep(0.2)
                            print(f'Número secreto: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')
                            break

            if digitos_certos == 0:
                time.sleep(0.2)
                print('\nVocê não acertou nenhum dígito dessa vez...')

            digitos_certos = 0
            time.sleep(0.2)
            print(f'\nfaltam {10-tentativas} tentativa(s)...') 

            if tentativas >= 5:
                time.sleep(0.2)
                print(f'\nVou te dar uma dica!!')
                if dica_maior_menor == 1:
                    if primeiro_digito != x:
                        if a > x:
                                time.sleep(0.2)
                                print(f'==> O primeiro dígito é menor que {a}')
                                primeiro_digito = f'<{a}'
                        else:
                            time.sleep(0.2) 
                            print(f'==> O primeiro dígito é maior que {a}')
                            primeiro_digito = f'>{a}'
                    elif segundo_digito != y:
                        if b > y:
                                time.sleep(0.2)
                                print(f'==> O segundo dígito é menor que {b}')
                                segundo_digito = f'<{b}'
                        else:
                            time.sleep(0.2)
                            print(f'==> O segundo dígito é maior que {b}')
                            segundo_digito = f'>{b}'
                    elif terceiro_digito != z:           
                        if c > z:
                                time.sleep(0.2)
                                print(f'==> O terceiro dígito é menor que {c}')
                                terceiro_digito = f'<{c}'
                        else:
                            time.sleep(0.2)
                            print(f'==> O terceiro dígito é maior que {c}')
                            terceiro_digito = f'>{c}'
                    elif quarto_digito != w:           
                        if d > w:
                                time.sleep(0.2)
                                print(f'==> O quarto dígito é menor que {d}')
                                quarto_digito = f'<{d}'
                        else:
                            time.sleep(0.2)
                            print(f'==> O quarto dígito é maior que {d}')
                            quarto_digito = f'>{d}'
                        
                if dica_par_impar == 1:
                    if primeiro_digito != x:
                        if x % 2 == 0:
                            time.sleep(0.2)
                            print(f'==> O primeiro dígito é par!')
                            primeiro_digito = 'PAR'
                        else:
                            time.sleep(0.2)
                            print(f'==> O primeiro dígito é ímpar!')
                            primeiro_digito = 'ÍMPAR'

                    elif segundo_digito != y:
                        if y % 2 == 0:
                                time.sleep(0.2)
                                print(f'==> O segundo dígito é par!')
                                segundo_digito = 'PAR'
                        else:
                            time.sleep(0.2)
                            print(f'==> O segundo dígito é ímpar!')
                            segundo_digito = 'ÍMPAR'

                    elif terceiro_digito != z:
                        if z % 2 == 0:
                                time.sleep(0.2)
                                print(f'==> O terceiro dígito é par!')
                                terceiro_digito = 'PAR'
                        else:
                            time.sleep(0.2)
                            print(f'==> O terceiro dígito é ímpar!')
                            terceiro_digito = 'ÍMPAR'

                    elif quarto_digito != w:
                        if w % 2 == 0:
                                time.sleep(0.2)
                                print(f'==> O quarto dígito é par!')
                                quarto_digito = 'PAR'
                        else:
                            time.sleep(0.2)
                            print(f'==> O quarto dígito é ímpar!')
                            quarto_digito = 'ÍMPAR'
                                
                    dica_par_impar -= 1
                    dica_maior_menor += 1
            time.sleep(0.2)
            print(f'\nDigitos descobertos são: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')
            cont += 1
            time.sleep(0.4)
            input('\n<<< Tecle enter para próxima tentativa >>>')
            os.system('cls')

    while True: 
        time.sleep(0.2)
        jogar_novamente_ou_parar = (input('\nDeseja jogar novamente? 1 = SIM || 0 = NÃO: '))
        if jogar_novamente_ou_parar == '1':
            condicao_jogar_novamente_ou_parar = '0' 
            break
        elif jogar_novamente_ou_parar == '0': 
            condicao_jogar_novamente_ou_parar = '1'
            time.sleep(0.2)
            print('Finalizando app...')
            break
        if jogar_novamente_ou_parar != '1' or jogar_novamente_ou_parar != '0' or jogar_novamente_ou_parar == '':
            time.sleep(0.2)
            print('Entrada inválida!')