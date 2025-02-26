# # Uyga vazifa:
# # 21- mashq. Uchburchakning uchta tomonining krdinatalari berilgan . Shuning yuzasini hisoblash A(x1, y1), B(x2, y2), C(x3, y3):
# print('Koordinatalarini kirgizing A(x1, y1), B(x2, y2), C(x3, y3)')
# x1 = int(input("x1 - ")) ; y1 = int(input("y1 - "))
# x2 = int(input("x2 - ")) ; y2 = int(input("y2 - "))
# x3 = int(input("x3 - ")) ; y3 = int(input("y3 - "))
# a = ((x2-x1)**2 + (y2 - y1)**2)**(1/2)
# b = ((x3-x1)**2 + (y3 - y1)**2)**(1/2)
# c = ((x2-x3)**2 + (y2 - y3)**2)**(1/2)
# p = (a+b+c)/2 ; S = (p * (p-a)*(p-b)*(p-c))**(1/2)
# print ('Berilgan uchburchakning yuzi S - ',S)


# # 22 - mashq. Berilgan A va B sonlarnin o'rnini almashtirib chiqarish:
# A = int(input('A sonini kiriting A - ')) ; B = int(input('B sonini kiriting B - '))
# A, B = B, A
# print(f'YAngi qiymatlar A = {A}, B = {B}')

# # 25 -mashq. Berilgan funksiyani qiymatini topish.
# print('BErilgan funksiya: y = 3x ** 6 - 6x ** 2 - 7')
# x = float(input('x sonini kiriting  x - '))
# y = 3 * x**6 - 6*x**2 - 7
# print('Funksiya qiymat y =',y)

# Kvadrat tenglama yechadigan dastur tuzamiz.
print(' Kvadrat tenglama korinishi: Ax2+Bx+C=0')
A = float(input('A  koeffisentini kiriting A - ')) ; B = float(input('B  koeffisentini kiriting B - ')) ; C = float(input('C  koeffisentini kiriting C - '))
D = B**2 - 4*A*C
if D >= 0 :
    x1 = (-B + (D)/2)/2
    x2 = (-B - (D)/2)/2
    print(f'Tenglama yechimlari x1 = {x1}, x2 = {x2} ')
else :
    print('Tenglama ildizga ega emas')