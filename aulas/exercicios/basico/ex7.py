while True:
    res = None
    n1 = input('Primeiro valor: ')
    n2 = input('Segundo valor: ')
    try:
        n1 = float(n1)
        n2 = float(n2)
        
        operador = input('operador matematico: ')
        if len(operador) > 1:
            print('erro: possivelmente voce informou mais de 1 operador matematico')
            print('\n\n\n')
            continue
            
        if operador in '+-/x':
            if operador == '+':
                res = n1 + n2
            elif operador == '-':
                res = n1 - n2
            elif operador == '/':
                res = n1 / n2
            elif operador == 'x':
                res = n1 * n2   
               
        else:
            print('operadores validos: ( + , - , / , x )')
            print('\n\n\n')
            continue
    except:
        print('parece que voce nao informou numeros! tente denovo')
        print('\n\n\n')
        continue
    
    print(f'resultado: {res}')
    print('\n\n\n')
    
    continuar = input('continuar ou sair: ')
    if continuar == 'sair':
        break
    print('\n')