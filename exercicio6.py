#Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string 
#digitada. Imprima na tela somente os dois últimos caracteres da segunda variável tipo string.

frase = input('Digite uma frase qualquer: ')
tamanho = len(frase)

frase2 = frase[:int(tamanho/2)] # : (poderia usar 0:) está contando desde o 1° caractere até o fim e dividindo por 2,
#retornando inteiro para não quebrar.

print(frase2[-2:]) #macete do python para pegar os dois últimos caracteres: -2: