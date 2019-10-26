impostor = 11
inss = 8
sindicato = 5

salh = float(input("Informe quanto você ganha por hora: "))
horas = float(input("Agora informe quantas horas trabalhou no mês: "))

salbruto = salh * horas
vlrimpost = (salh + (salh * impostor / 100))
vlrinss = (salh + (salh * inss / 100))
vlrsindicato = (salh + (salh * sindicato / 100))

descontos = vlrsindicato + vlrinss + vlrimpost
salliq = salbruto - descontos
print('O salario bruto do funcionario é de R$',salbruto)
print('O valor total da soma dos impostos é de: R$',vlrimpost)
print('O valor de desconto para o sindicato é de: R$',vlrsindicato)
print('O valor de desconto para o INSS é de: R$',vlrinss)
print('O salario liquido do funcionario é de: R$',salliq)



