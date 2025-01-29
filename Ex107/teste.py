import moeda

d = float(input('Digite um numero: '))
print(f'A metade de {d} é {moeda.metade(d)}')
print(f'O dobro de {d} é {moeda.dobro(d)}')
print(f'O aumento de 20% é {moeda.aumentar(d,20)}')
print(f'Reduzindo em 20% é {moeda.diminuir(d,20)}')