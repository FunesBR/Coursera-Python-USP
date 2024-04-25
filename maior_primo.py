def maior_primo(x):
    if x >= 2:
        k=x
        éprimo(k)
    else:
        print("O número deve ser maior que 2")
 
def éprimo(k):
    x=k
    y=x-1

    while (x % y) != 0 and y > 0:
        y = y-1 
    if y<=1:
        return(x, "primo")
    else: 
        print("não primo")
