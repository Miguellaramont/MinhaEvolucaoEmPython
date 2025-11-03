#Calculo de salário e desconto
valorH = int(input('Informe o valor da sua hora:'))
QuantH = int(input('Informe a quantidade de horas trabalhadas: '))
salario_bruto = valorH * QuantH
print(F'Salário Bruto   :R$ {salario_bruto}')
ir = salario_bruto*0.05
inss = salario_bruto*0.10
fgts = salario_bruto*0.08

print(F'IR(5%)          :R$ {ir}')
print(F'INSS(10%)       :R$ {inss}')
print(F'FGTS(8%)       :R$ {fgts}')
total_desconto = ir + inss
print(F'Total de descontos     :R$ {total_desconto}')
salario_liquido = salario_bruto - total_desconto
print (F'Salário Liquido       :R$ {salario_liquido}')