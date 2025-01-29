from Ex115.menu import *

def conferir(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False

    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve algum erro ao criar o aquivo')
    else:
        print(f'Arquivo {nome} criado com Sucesso! :)')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir arquivo :(')
    else:
        cabe("Pessoas cadastradas")
        print(a.read())

