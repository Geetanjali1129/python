n=int(input('enter a number'))
a=0
b=1
print(a)
print(b)
count=3
while count<=n:
    s=a+b
    print(s)
    a=b
    b=s
    count+=1
