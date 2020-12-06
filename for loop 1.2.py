s=int(input('enter a start number'))
e=int(input('enter a end number'))
b=int(input('enter a number'))
if s<=e:
    for n in range(s,e+1):
        print(n,'*',b,'=',n*b)
else:
    for n in range(s,e-1,-1):
        print(n,'*',b,'=',n*b)
