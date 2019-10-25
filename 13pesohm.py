#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

print("=============================================")
print(" Tabela de peso ideal para determinado sexo")
print("=============================================")
h = float(input("Informe sua altura: "))
print("Agora informe se você é Homem ou Mulher: ")
print("[1] - Homem")
print("[2] - Mulher")
oper = int(input(" "))

if oper == 1:
	pesoi = ((72.7*h) - 58)
elif oper == 2:
	pesoi = ((62.1*h) - 44.7)
else:
	print("Informação não corresponde a nenhum sexo.")

print("O peso ideal é: ", pesoi)
