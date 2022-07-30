aulfhi = int(input())
if (aulfhi  % 4 == 0) and ( aulfhi % 100 != 0 ):
    print(1)

elif aulfhi  % 400 == 0:
    print(1)

else:
    print(0)
