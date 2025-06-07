'''
#Condição com OR
#Verifique se o usuario pode ganhar um brinde se ele for cliente VIP ou se gastar mais de R$500.00. User OR na condição

#Forma 1(Armazenando)
VIP = True
valor_gasto = 200

if VIP or valor_gasto > 500:
    print("Brinde Disponivel")
else:
    print("Brinde Indisponivel")


#Forma 2(Perguntando)
cliente_vip = input("É cliente vip? (s/n)") == "s"  #(Pergunta é realizada mas ja possui uma resposta(dado) armazenada)
gasto = float(input("Valor gasto:"))

if cliente_vip or gasto > 500:
    print("Ganhou Brinde!")
else:
    print("Sem Brinde")
'''