num = int(input('Informe um número: '))
divisor = int(input('Agora informe o divisor: '))
total = 0
aux = num
lista = []
while num > 0:
    if (num % divisor == 0):
        lista.append(num)
        total = total + 1
    num = num - 1
print(lista)
print(f'Dentre os {aux} valores, o total de divisiveis por {divisor} foi {total}')