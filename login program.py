mid="thub@gmail.com"
ipw='1234'
for i in range(5):
    umid=input('enter a mail id')
    upwd=input('enter password')
    if umid==mid and upwd==ipw:
        print('login successfully')
        break
    else:
        print('wrong credentials')
else:
    print('account blocked')
