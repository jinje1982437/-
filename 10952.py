aj = 1
while aj < 10:
    hgn, Eiu = input().split()
    hgn = int(hgn)
    Eiu = int(Eiu)
    if hgn < 1 and Eiu < 1: 
        break
    print(hgn + Eiu)
