x=int(input("Digite um número inteiro: "))

def primo(x):
    y=x-1
    while (x % y) != 0 and y > 0:
        y = y-1 
    if y<=1:
        return True
    else: 
        return False


while x>0:
    if primo(x):
        print (f"{x} é primo")
    else:
        print(f"{x} não é primo")
    x=int(input("Digite um número inteiro: "))
