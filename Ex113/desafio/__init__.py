def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO!!!!! digite um numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mERRO!!!!! usuario não informou nada\033[m')
            return 0
        else:
            return n


def LeiaReal(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError)  :
            print(f'\033[31mERRO!!!!! digite um numero real valido\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mERRO!!!!! usuario não informou nada\033[m')
            return 0
        else:
            return r


def resumo(n=0, p=0):
    print(f'O valor inteiro é {n} e o valor real é {p}')