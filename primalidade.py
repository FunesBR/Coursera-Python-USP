x=int(input("Digite um número inteiro: "))
y=x-1

while (x % y) != 0 and y > 0:
    y = y-1 
if y<=1:
    print("primo")
else: 
    print("não primo")