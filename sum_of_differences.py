s= [int(x) for x in input().split()]
s.sort()
a=s[1]-s[0]
b=s[2]-s[1]
print(a+b)