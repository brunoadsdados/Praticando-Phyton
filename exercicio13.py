#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de KWh 
#consumida e o tipo de instalação: R para residências, I para Indústrias, e C para comércios.

#Calcule o preço de acordo com a tabela a seguir:

#   Preço por tipo e faixa de consumo
#  Tipo:        Faixa(KWh):      Preço(R$):
#Residencial    até 500            0,40
#Residencial    Acima de 500       0,65
#Comercial      Até 1000           0,55
#Comercial      Acima de 1000      0,60
#Industrial     Até 5000           0,55
#Industrial     Acima de 5000      0,60

kwh = float(input("Qual a quantidade de Kwh consumidos? "))

print("INSTALAÇÃO:")
print("R - Residências")
print("C - Comércios")
print("I - Indústrias")

instalacao = input("Escolha o tipo de instalação: ")

if (instalacao == "R" or "r"):
    if kwh > 500:
        preco = 0.65
    else:
        preco = 0.40
    print(f'Você consumiu {kwh} kWh e o total a pagar é de R${kwh * preco}')
    

elif (instalacao == "C" or "c"):
    if kwh > 1000:
        preco = 0.60
    else:
        preco = 0.55
    print(f'Você consumiu {kwh} kWh e o total a pagar é de R${kwh * preco}')

elif (instalacao == "I" or "i"):
    if kwh > 5000:
        preco = 0.55
    else:
        preco = 0.60
    print(f'Você consumiu {kwh} kWh e o total a pagar é de R${kwh * preco}')

else:
    print("Instalação inválida! Encerrando o programa...")