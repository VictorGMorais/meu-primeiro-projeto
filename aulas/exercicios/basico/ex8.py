import os
palavra_secreta = 'ana'
letras_acertadas = ''
t = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Apenas uma letra por vez!')
        continue
    t += 1
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'      
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(
          f'PARABENS VOCE CONSEGUIU ACERTAR A PALAVRA SECRETA!\n\
            USOU APENAS {t} TENTATIVAS!\n\
            A PALAVRA SECRETA ERA : {palavra_secreta}'
            )
        letras_acertadas = ''
        t = 0
        cont = input('Continuar? [s/n]')
        if cont == 'n':
            break