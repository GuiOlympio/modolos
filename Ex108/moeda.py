from sympy import false


def metade (n=0, form = False):
    '''
    -> Dividindo o parametro
    :param n: parametro a ser mudado
    :param form: sistema monetario real
    :return: res
    '''
    res = n / 2
    return res if not form else moeda(res)

def dobro(n=0, form = False):
    res = n * 2
    return res if not form else moeda(res)

def aumentar (n=0,p=0, form = False):
    res = n + (n* (p/100))
    return res if not form else moeda(res)

def diminuir (n=0,p=0 , form = False):
    res = n - (n * (p/100))
    return res if not form else moeda(res)

def moeda (n: object = 0, moeda: object = 'R$ ') -> object:
    return f'{moeda}{n:.2f}'.replace('.',',')