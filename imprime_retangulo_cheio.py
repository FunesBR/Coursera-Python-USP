largura=int(input("digite a largura: "))
altura=int(input("digite a altura: "))
lar=0
alt=0

while alt<altura:
    lar=0
    while lar<largura:
        lar=lar+1
        print("#", end="")
        if lar==largura:
            print("")
            alt=alt+1

