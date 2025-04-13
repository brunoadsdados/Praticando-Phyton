#Execute as seguintes atribuições:
# s1 = 'ant'
s1 = 'ant'

# s2 = 'bat'
s2 = 'bat'

#s3 = 'cod'
s3 = 'cod'

#Agora, utilizando operadores + e *, crie as saídas a seguir:

# a) 'ant bat cod'
resA = s1 + ' ' + s2 + ' ' + s3
print(resA)

# b) 'ant ant ant ant ant ant ant ant ant ant'
resB = 10 * (s1 + ' ')
print(resB)

# c) 'ant bat bat cod cod cod'
resC = (s1 + ' ') + ((s2 + ' ') * 2) + ((s3 + ' ') * 3)
print(resC)

# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
resD = (s1 + ' ' + s2 + ' ') * 7
print(resD)

# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod
resE = (s2 * 2 + s3 + ' ') * 5
print(resE)