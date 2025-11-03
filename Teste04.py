lista = []
tam = int(input('Informe quantos números vc quer contar: '))
for i in range(tam):
    num = int(input(f'Informe o {i+1}° número:'))
    lista.append(num)
lista.reverse()
print(f'Sua lista invertida é {lista}')