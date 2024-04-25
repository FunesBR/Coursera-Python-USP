x=int(input("Digite um número inteiro: "))
y= 1
z =()
sim=False

while x > 0 :
    y = x%10
    x = x//10
    
    if y == z:
        sim=True
        break
    else:
        z = y
        sim=False

if sim == True:
    print("sim")
else:
    print("nao")
    
