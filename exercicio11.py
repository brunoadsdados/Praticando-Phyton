#Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se 
#os valores formam um triângulo e classifique como:

#Lembre-se: Para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma
#dos outros dois (exercicio da apostila - aula 3)

# a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)

ladoA = int(input("Informe o valor do lado A: "))
ladoB = int(input("Informe o valor do lado B: "))
ladoC = int(input("Informe o valor do lado C: "))

if ((ladoA > 0 and ladoB > 0 and ladoC > 0) and (ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA)):
#Se chegou até aqui é porque o triângulo é válido.
    if (ladoA != ladoB and ladoA != ladoC and ladoB != ladoC):
        print("Triângulo escaleno")
    else:
        if (ladoA == ladoB and ladoB == ladoC):
            print("Triângulo equilátero")
        else:
            print("Triângulo isósceles")
else:
    print("Ao menos um dos valores indicados não servem para formar um triângulo!")