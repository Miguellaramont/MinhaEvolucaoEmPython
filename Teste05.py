lista = []
num = 0
resp = 's'
while resp != 'n':
   resp = str(input('Você deseja adicionar um número?'))
   resp.lower()
   if resp == 's':
       num = int(input('Então informe um número: '))
       lista.append(num)
   elif resp == 'n':
       print ('ENCERRANDO...')
   else:
       print('Esta opção  não é válida! Tente novamente')
print(lista)
maior = max(lista)
print(f'Dentre estes números, o maior deles é {maior}')