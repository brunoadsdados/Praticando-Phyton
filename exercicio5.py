#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade
#de dias pelos quais o carro foi alugado. CAlcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por
#km rodado.

qtdeKm = float(input('Qual a quantidade de quilômetros percorrida? '))
dias = int(input('Por quantos dias você alugou o carro? '))

precoDia = dias * 60
precoKm = qtdeKm * 0.15
precoFinal = precoDia + precoKm

print(f'Você alugou o carro por {dias} dias e rodou {qtdeKm} quilômetros!')
print(f'O preço a pagar pelo aluguel do carro é de: R${precoFinal}')