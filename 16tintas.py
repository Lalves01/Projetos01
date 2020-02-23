#Verificação de metros quadrados por lata de tinta
#1ºPedir o tamanho de metros quadrados a ser pintado
#2º1Lt de tinta pintam 3m 
#3ºCada lata de tinta contém 18Lt
#4ºCada lata vale R$80,00
#5º uma lata pinta 54m

metros = int(input("Informe quantos metros serão pintados: "))

quantia = metros / 54

print ("Você precisará de", quantia, "de latas.")
print("E o valor total será de R$", quantia * 80)
