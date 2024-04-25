largura=int(input("digite a largura: "))
altura=int(input("digite a altura: "))
lar=0
alt=0

while alt<altura:
    lar=0
    while lar<largura:
            if alt == 0 or alt == altura-1 or lar == 0 or lar == largura-1:
                print("#", end="")
                lar=lar+1
            else:
                print(" ", end="")
                lar=lar+1
            if lar==largura:
                print("")
                alt=alt+1
