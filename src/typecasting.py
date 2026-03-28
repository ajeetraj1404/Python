# Explicit typecasting
a = 10
b = '20'
c = a + int(b)
print(c,type(c))

#Implicit typecasting highest order type converts the lower order
a = 10 # int
b = 2.2 # float
c = 10 + 2.2 # 10 converted to float
print(c,type(c))
