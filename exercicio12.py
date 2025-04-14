#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: 
#adição(+), subtração(-), multiplicação(*), ou divisão(/). Exiba na tela o resultado da operação desejada (exercício
#da apostila - aula 3)

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))


print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

operacao = int(input("Escolha uma operação: "))

if (operacao == 1):
    resultado = n1 + n2
    print(f'Você escolheu a operação de soma, o resultado é {resultado}.')
else:
    if (operacao == 2):
        resultado = n1 - n2
        print(f'Você escolheu a operação de subtração, o resultado é {resultado}.')
    else:
        if (operacao == 3):
            resultado = n1 * n2
            print(f'Você escolheu a operação de multiplicação, o resultado é {resultado}.')
        else:
            if (operacao == 4):
                resultado = n1 / n2
                print(f'Você escolheu a operação de divisão, o resultado é {resultado}.')
            else:
                print("Operação inexistente!")
    
