#Traduza as afirmações a seguir para condicionais em python:

#a) Se idade é maior que 60, escreva: "Você tem direito aos benefícios"
idade = int(input("Digite sua idade: "))
if (idade > 60):
    print(f'Você tem {idade} anos, portanto, tem direito aos benefícios!')
else:
    print(f'Você tem {idade} anos, portanto, não tem direito aos benefícios!')

#b) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você está morto!"
dano = int(input('Digite o valor do dano: '))
escudo = int(input('Digite o valor do escudo: '))
if (dano > 10 and escudo == 0):
    print("Você está morto!")


#c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva "Você escapou!"
norte = False
sul = True
leste = False
oeste = False

if (norte or sul or leste or oeste == True):
    print("Você escapou!")
else:
    print("Você não escapou!")