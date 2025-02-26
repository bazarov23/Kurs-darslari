d = int(input('d = '))
m = int(input('m = '))
y = int(input('y = '))

kabisa = False
if y%4==0:
    kabisa = True
if y%100==0 and y%400!=0:
    kabisa = False

d = d + 1

if m==4 or m==6 or m==9 or m==11:
    if d>30:
        d = 1
        m = m+1
elif m==2:
    if d > 28 + kabisa:
        d = 1
        m = 3
else:
    if d > 31:
        d = 1
        m = m + 1
    if m > 12:
        m = 1
        y = y + 1

print(d,m,y,sep='.')