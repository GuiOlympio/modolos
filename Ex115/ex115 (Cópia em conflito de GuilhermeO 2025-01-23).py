from Ex115.menu import *
from Ex115.menu.arquivo import *

arq = 'cadastropessoa.txt'
if not conferir(arq):
    criarArq(arq)

while True:
    opc = menu(['Ver Pessoa Cadastrada' , 'Cadastrar Pessoa', 'Sair do Sistema'])
    if opc == 1:
        lerArq(arq)
    elif opc == 2:
        cabe('Cadastrar Pessoa'.center(30))
    elif opc == 3:
        cabe('Sair do Sistema... até logo :)'.center(30))
        break
    else:
        print(f'\033[31mERRO!!!!! Opção invalida\033[m')