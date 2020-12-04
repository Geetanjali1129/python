p=float(input('enter percentage'))
bl=int(input('enter no of backlogs'))
if p>=60 and bl==0:
    print('eligible')
else:
    print('not eligible')
