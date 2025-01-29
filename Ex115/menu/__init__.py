def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO!!!!! Selecione um opção valida\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mERRO!!!!! usuario não informou nada\033[m')
            return 0
        else:
            return n

def linha(tam = 20):
    print('=*'*tam)
    return linha


def cabe(txt):
    linha()
    print(txt)
    linha()

def menu(lista):
    c = 0
    for item in lista:
        print(f'{c+1} - {item} ')
        c += 1
    opc = leiaInt('Sua opção: ')
    return opc

