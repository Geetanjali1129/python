n=int(input('enter a number'))
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    s=a+b
    print(s)
    a=b
    b=s
