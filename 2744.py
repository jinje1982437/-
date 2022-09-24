l = ''
x = input()
for o in x:



               

    if 96 < ord(o) < 123:
     l = l + o.upper()
    else:
        l = l + o.lower()
print( l )
