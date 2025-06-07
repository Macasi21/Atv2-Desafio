
#Veriricar multiplos de 3 e 5
#Receba um numero do usuario e diga se ele é multiplo de 3, de 5, de ambos ou de nenhuma.

numero = int(input("Digite um numero:"))

if numero % 3 == 0 and numero % 5 == 0:
    print("é Multiplo de 3 e 5")
elif numero % 3 == 0:
    print ("É multiplo de 3")
elif numero % 5 == 0:
    print("É multiplo de 5")
else:
    print("Não é multiplo de 3 ou 5")
