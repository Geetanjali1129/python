n=int(input('enter a number'))
a=n
s=0
while n>0:
    rem=n%10
    s+=rem*rem*rem
    n=n//10
    if a==s:
        print(a,'is Armstrong number')
    else:
        print(a,'is not a Armstrong number')
