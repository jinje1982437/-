a ,s ,k = input().split(' ')
a2 = int(input())
a = int(a)
s = int(s)
k = int(k) +a2

s = s + int(k / 60)
k = k % 60


a = a + int(s / 60)
s = s % 60


a = a % 24
print(a,s,k)
