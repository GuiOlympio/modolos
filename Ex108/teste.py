from Ex108 import moeda

d = float(input('Digite um numero: '))
print(f'A metade de {moeda.moeda(d)} é {(moeda.metade(d, True))}')
print(f'O dobro de {moeda.moeda(d)} é {(moeda.dobro(d,True))}')
print(f'O aumento de 20% é {(moeda.aumentar(d,20,True))}')
print(f'Reduzindo em 20% é {(moeda.diminuir(d,20, True))}')
