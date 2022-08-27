iudr = int(input())
for row in range( iudr ):
    for col in range( iudr ):
    #   print( '*', end = " " )
      if row > col:
          print("", end = "")
      else:
          print("*", end = "")
    print()
