from sqlalchemy import True_
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

def resumo (n=0, taxaa=0, taxar=0):
    print("=+"*30)
    print("RESUMO DO VALOR".center(30))
    print("=+" * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(n, taxaa, True)} ')
    print(f'{taxar}% de desconto: \t{diminuir(n, taxar,True)}')
    print("=+" * 30)