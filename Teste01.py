#Revisão de atividade antiga
quant_notas = int(input('Informe quantas notas serão registradas:'))
lista = []
for i in range(quant_notas):
    notas = float(input(f'Digite a {i+1}° nota:'))
    lista.append(notas)
print(lista)
media = sum(lista) / len(lista)
if (media == 6):
    print(f'Você está na media! Você ficou com {media:.2f} pontos')
elif media > 6:
     print(f'Você foi aprovado! Você ficou com {media:.2f} pontos')
else:
     print(f'Você foi reprovado! Você ficou com {media:.2f} pontos')