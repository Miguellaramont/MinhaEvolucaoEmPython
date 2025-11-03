# 1°: x=+ y=+
# 2°: x=- y=+
# 3°: x=- y=-
# 4°: x=+ y=-
x = 1
y = 2
while (x != 0) and (y != 0):
    x = int(input('Informe a abiscissa:'))
    y = int(input('Informe a ordenada:'))
    print ('+-----------------------------------+')

    if x > 0 and y > 0:
        print ('Você esta no 1° quadrante')
    elif x < 0 and y > 0:
        print ('Você esta no 2° quadrante')
    elif x < 0 and y < 0:
        print ('Você esta no 3° quadrante')
    elif x > 0 and y < 0:
        print ('Você esta no 4° quandrante')
    print ('+-----------------------------------+')
print ('ENCERRANDO...')
