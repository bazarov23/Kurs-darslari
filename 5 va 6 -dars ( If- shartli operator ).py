# Mavzu: Shartli operatorlar(if, elif, else)


# # 1 masala. Agar berilgn son musbat bolsa 1 ga oshirilsin , aks xolda ozgartirilmasin
# a = int(input("a - "))
# if a > 0:
#     print(a +1)
# elif a <= 0:
#     print(a)

# # 3 masala. Agar berilgn son musbat bolsa 1 ga oshiring, manfiy bolsa 2 ga kamaytiring, agar 0 bolsa 10 ga teng deb chiqarsin
# a = int(input("a - "))
# if a > 0:
#     print(a +1)
# elif a < 0:
#     print(a-2)
# elif a == 0:
#     print (a+10)

# # 4 masala. Uchta butun son berilgan , shu sonlar orasidan nechtasi musbatligini korsatadigan dastur
# a = int(input("a - ")); b = int(input("b - ")); c = int(input("c - "))
# x, y, z = 0, 0, 0
# # a ni tekshirish
# if a > 0: x += 1
# elif a < 0: y += 1
# else : z += 1
# # b ni tekshiramiz
# if b>0: x += 1
# elif b<0: y +=1
# else: z += 1
# # c ni tekshiramiz
# if c>0: x += 1
# elif c<0: y+=1
# else: z +=1
# print(x,"ta musbat",y,"ta manfy",z,"ta nol bor")

# # 6 masala. 2 ta butun son berilgan, qaysi bir kattaligini aniqlovchi dasyur
# a = int(input("a - ")); b = int(input("b - "))
# if a>b:
#     print(f" {a} katta {b} dan")
# elif a<b:
#     print(f" {b} katta  {a} dan")
# elif a==b:
#     print(f" {a} ga teng  {b}")

# # 9 masala. a va b sonlar berilgan, ularni shunday ozgartirish kerakki a son katta b son kichik bolsin va ekranga chiqsin
# a = int(input("a - ")); b = int(input("b - "))
# if a>b:
#     print(f" {a} katta {b} dan")
# elif a<=b:
#     a = b +1
#     print(f" {a} katta  {b} dan")

# #12 masala. 3 ta butun son berilgan ularni kichigini topuvchi dastur
# a = int(input("a - ")); b = int(input("b - ")); c = int(input("c - "))
# if a<=b and a<=c:
#     print(f"{a} eng kichigi")
# elif b<=a and b<=c:
#     print(f"{b} eng kichigi")
# elif c<=a and c<=b or a==b==c:
#     print(f"{c} eng kichigi")

# #14 masala. 3 ta butun son berilgan avval eng kichigini keyin kattasini ekranga chiqaring
# a = int(input("a - ")); b = int(input("b - ")); c = int(input("c - "))
# if a<=b<=c:
#     print(f"{a} eng kichigi {c} eng kattasi")
# elif b<=a<=c:
#     print(f"{b} eng kichigi {c} eng kattasi")
# elif c<=a<=b or a==b==c:
#     print(f"{c} eng kichigi {b} eng kattasi ")
# elif a<=c<=b:
#     print(f"{a} eng kichigi {b} eng kattasi")
# elif b<=c<=a:
#     print(f"{b} eng kichigi {a} eng kattasi")
# elif c<=b<=a:
#     print(f"{c} eng kichigi {a} eng kattasi")

# #15 masala. 3 ta butun son berilgan yigindisi eng katta boladigan 2 ta si ekranga chiqarilsin
# a = int(input("a - ")); b = int(input("b - ")); c = int(input("c - "))
# if a<=c and a<=b:
#     print(f"{b} va {c} shu ikkalasini qoshilsa yigindi katta boladi. Yigindi {c+b}")
# elif b<=a<=c or b<=c<=a:
#     print(f"{a} va {c} shu ikkalasini qoshilsa yigindi katta boladi. Yigindi {a+c}")
# elif c<=a<=b or c<=b<=a:
#     print(f"{a} va {b} shu ikkalasini qoshilsa yigindi katta boladi. Yigindi {a+b}")
# elif c==a==b:
#     print(f"{a},{b},{c} uchala son xam bir biriga teng{a+b+c}")

# #19 masala. 3 ta butun son berilgan yigindisi eng katta boladigan 2 ta si ekranga chiqarilsin
# a = int(input("a - ")); b = int(input("b - ")); c = int(input("c - ")); d = int(input("d - "))
# if a==b==c!=d:
#     print(f"{d} soni 4 chi tartibdagi son")
# elif a==b==d!=c:
#     print(f"{c} soni 3 chi tartibdagi son")
# elif a==c==d!=b:
#     print(f"{b} soni 2 chi tartibdagi son")
# elif c==d==b!=a:
#     print(f"{a} soni 1 chi tartibdagi son")
# elif a==b==c==d:
#     print("Mos sonlar kiritilmadi")
# else:
#     print("Mos sonlar kiritilmadi")

# #23 masala togri tortburchakning 4 chi uchini topish
# x1, y1 = map(int, input("x1, y1 - ").split()); x2, y2 = map(int, input(" x2, y2 - ").split()) ; x3, y3 = map(int, input("x3, y3 - ").split())
# if x1==x2 and y2==y3:
#     print(f"x4-{x3},y4-{y1}")
# elif x3==x2 and y2==y1:
#     print(f"x4-{x1},y4-{y3}")
# else:
#     print(" Togri tortburchak yasab bolmaydi bu koordinatalar bilan")

# # 24 masala .
# from math import *
# x = int(input("x - "))
# if x>0:
#     N = 2*sin(x)
#     print(f"2*sin(x)= {N}")
# elif x<=0:
#     N = x-6
#     print(f"x -6 = {N}")

# #27 masala
# x = float(input("x - "))
# if x<0:
#     print("Natija = 0 ")
# elif  2*(x//2) <= x < 2*(x//2)+1 :
#     print("Natija = 1 ")
# elif  2*(x//2)+1 <= x < 2*(x//2)+2 :
#     print("Natija = -1 ")

# # 28 masala  Yilda necha kun bor
# x = int(input("Yilni kiriting - "))
# if (x % 4==0 and x % 100 != 0) or x % 400 == 0 :
#     print(f"{x} chi yilda 366 kun bor")
# else:
#     print(f"{x} chi yilda 365 kun bor")

# # 29 masala: Sonni tavsiflash
# x = int(input("Son kiriting - "))
# if x>0 and x%2 ==0:
#     print(f"{x}  Musbat juft son")
# elif x<0 and x%2 ==0:
#     print(f"{x}  Manfiy juft son")
# elif x<0 and x%2 ==1:
#     print(f"{x}  Manfiy toq son")
# elif x>0 and x%2 ==1:
#     print(f"{x}  Musbat toq son")
# elif x==0:
#     print(f"{x}  Nol")

# # 30 masala. 1-999 oraliqda son berilgan. uni xam tasvirlash kerak
# x = int(input("Son kiriting - "))
# if x>0 and x%2 ==0 :
#     if x//10 == 0:
#         print(f"{x}  Bir honali musbat juft son")
#     elif x//100 == 0:
#         print(f"{x}  ikki honali musbat juft son")
#     elif  x//1000 == 0:
#         print(f"{x}  Uch xonali musbat juft son")
# elif x<0 and abs(x)%2 ==0:
#     if abs(x)//10 == 0:
#         print(f"{x}  Bir honali manfiy juft son")
#     elif abs(x)//100 == 0:
#         print(f"{x}  ikki honali manfiy juft son")
#     elif abs(x)//1000 == 0:
#         print(f"{x}  Uch xonali manfiy juft son")
# elif x<0 and abs(x)%2 == 1:
#     if abs(x)//10 == 0:
#         print(f"{x}  Bir honali manfiy toq son")
#     elif abs(x)//100 == 0:
#         print(f"{x}  ikki honali manfiy toq  son")
#     elif abs(x)//1000 == 0:
#         print(f"{x}  Uch xonali manfiy toq  son")
# elif x>0 and x%2 ==1:
#     if x//10 == 0:
#         print(f"{x}  Bir honali musbat toq son")
#     elif x//100 == 0:
#         print(f"{x}  ikki honali musbat toq  son")
#     elif x//1000 == 0:
#         print(f"{x}  Uch xonali musbat toq  son")
# elif x==0:
#     print(f"{x}  Nol")

# # Masala Junyor: 1 dan 99 gacha son kiritiladi shuni soz bilan ifodalash kk
# a = int(input('a - '))
# if 0<a<100:
#     qoldiq = a% 10
#     son = ""
#     if 9 < a < 20:
#         son = "o'n"
#     elif 19 < a < 30:
#         son = "yigirma"
#     elif 29 < a < 40:
#         son = "o'ttiz"
#     elif 39 < a < 50:
#         son = "qirq"
#     elif 49 < a < 60:
#         son = "ellik"
#     elif 59 < a < 70:
#         son = "oltmish"
#     elif 69 < a < 80:
#         son = "yetmish"
#     elif 79 < a < 90:
#         son = "sakson"
#     elif 89 < a < 100:
#         son = "to'qson"
#     if qoldiq == 1:
#         son += " bir"
#     elif qoldiq == 2:
#         son += " ikki"
#     elif qoldiq == 3:
#         son += " uch"
#     elif qoldiq == 4:
#         son += " to'rt"
#     elif qoldiq == 5:
#         son += " besh"
#     elif qoldiq == 6:
#         son += " olti"
#     elif qoldiq == 7:
#         son += " yetti"
#     elif qoldiq == 8:
#         son += " sakkiz"
#     elif a% 10 == 9:
#         son += " toqqiz"
#     print(son)
# else:
#     print(" 1 dan 100 gacha son kiriting")
#









