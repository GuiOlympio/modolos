def texto(msg):
    print(f'R$ {msg} ', end='')
    return msg

def metade(n):
    res = n / 2
    texto(res)
    return res

def dobro(n):
    res = n * 2
    texto(res)
    return res

def aumentar (n,p):
    res = n + (n* (p/100))
    texto(res)
    return res

def diminuir (n,p):
    res = n - (n * (p/100))
    texto(res)
    return res