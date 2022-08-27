j = int( input() ) 
for row in range( j ):
    for col in range( j ):
    #   print( '*', end = " " )
      if row > col:
          print("", end = " ")
      else:
          print("*", end = "")
    print()
