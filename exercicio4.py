#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. 
#Calcule e exiba o valor do desconto e o preço do produto.

precoProduto = float(input('Digite o preço do produto: R$'))
percentualDesconto = float(input('Digite o desconto aplicado ao produto (0 a 100%): '))

desconto = precoProduto * (percentualDesconto / 100)
precoFinal = precoProduto - desconto

print(f'O preço do produto é R${precoProduto}. O desconto é de {percentualDesconto}%')
print(f'O valor calculado de desconto é de R${desconto} e o valor final do produto é: R${precoFinal}')