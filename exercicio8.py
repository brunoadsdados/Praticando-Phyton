#Escreva as seguintes expressões booleanas em linguagem python:

#a) 1387 é divisível por 19:
if (1387 % 19 == 0): #Se o resto da divisão de 1387 por 19 = 0.
       print("Verdadeiro")
else:
    print("Falso")


#b) 31 é par:
if (31 % 2 == 0):
    print("Par")
else:
    print("ímpar")

#c) O menor valor entre, 34, 29 e 31 é menor que 30:

if(min(34, 29, 31) < 30):
    print("Verdadeiro")
else:
    print("Falso")