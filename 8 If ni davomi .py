# Dars davomi

# # Uyga vazifa. Yil oy kun kiritiladi, keyingi kunni topuvchi dastur tuzamiz.

kun = int(input("Kunni kiriting - "))
oy = int(input("Oyni kirting - "))
yil = int(input("Yilni kiriting - "))
print("kun.oy.yil", end="  ")
if 1<=kun<=31 and 1<=oy<=12:
    kun = kun + 1
    if (yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0:        # kabisa yilini tekshirish
        if  oy == 2 and  kun > 29:
            kun = 1; oy += 1
    else:
        if oy == 2 and kun > 28:
            kun = 1;oy += 1
        elif oy == 4 or oy == 6 or oy == 9 or oy == 11:
            if kun > 30:
                 kun = 1;oy += 1
        else:
             if kun > 31:
                   kun = 1; oy += 1
             if oy > 12:
                  oy = 1; yil += 1
    print(kun, oy, yil)
else:
    print(" Notog'ri sana kiritdingiz")



# # 8 mashqdan 11 masala Case11. Lokatr dunyoning bir tomoniga qaratilgan ("s"-shimol, "j"-janub, "q"-sharq, "g"-g'arb) va uchta raqamli kamanda:
# #  0-o`ngga buril, 1-chapga buril, 2-burilish 180°. C - lakatrning boshlang`ich holati va K1, K2 kamandalar berilgan.
# # Berilgan kamanda bajarilgandan keying lakatr holatini aniqlovchi -programma tuzilsin.
#
# c = input(" Boshlangich xolatini kiriting - ")
# print("Kamanda: 0-o`ngga buril, 1-chapga buril, 2-burilish 180°")
# k1 = int(input("Birinchi komanda - ")); k2 = int(input("Ikkinchi komanda - "))
# if c == "shimol" :
#     if (k1==1 and k2==0) or (k1==0 and k2==1) or (k1==2 and k2==2):
#         print(" 'shimol' ga qarab turibdi ")
#     elif (k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2):
#         print(" 'G'arb' ga qarab turibdi ")
#     elif (k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2):
#         print(" 'sharq' ga qarab turibdi ")
#     elif (k1 == 0 and k2 == 0) or (k1 == 1 and k2 == 1):
#         print(" 'Janub' ga qarab turibdi ")
# elif c == "janub" :
#     if  (k1==1 and k2==0) or (k1==0 and k2==1) or (k1==2 and k2==2) :
#         print(" 'Janub' ga qarab turibdi ")
#     elif (k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2):
#         print(" 'sharq' ga qarab turibdi ")
#     elif (k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2):
#         print(" 'G'arb' ga qarab turibdi ")
#     elif  (k1==0 and k2==0) or (k1==1 and k2==1):
#         print(" 'shimol' ga qarab turibdi ")
# elif c == "garb":
#      if (k1==1 and k2==0) or (k1==0 and k2==1) or (k1==2 and k2==2):
#          print(" 'Garb' ga qarab turibdi ")
#      elif (k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2):
#          print(" 'Janub' ga qarab turibdi ")
#      elif (k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2):
#          print(" 'shimol' ga qarab turibdi ")
#      elif  (k1==0 and k2==0) or (k1==1 and k2==1):
#          print(" 'sharq' ga qarab turibdi ")
# elif c == "sharq" :
#     if (k1==1 and k2==0) or (k1==0 and k2==1) or (k1==2 and k2==2):
#         print(" 'Sharq' ga qarab turibdi ")
#     elif (k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2):
#         print(" 'Shimol' ga qarab turibdi ")
#     elif (k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2):
#         print(" 'Janub' ga qarab turibdi ")
#     elif (k1==0 and k2==0) or (k1==1 and k2==1):
#         print(" 'Garb' ga qarab turibdi ")
# else:
#     print("Noto'g'ri kamanda berdingiz")
#
#               # 11 masalani 2- Usuli
#
#
# c = str(input(" Boshlangich xolatini kiriting - "))
# print("Kamanda: 0-o`ngga buril, 1-chapga buril, 2-burilish 180°")
# k1 = int(input("Birinchi komanda - ")); k2 = int(input("Ikkinchi komanda - "))
#
# if c == "shimol" and ((k1 == 1 and k2 == 0) or (k1 == 0 and k2 == 1) or (k1 == 2 and k2 == 2))\
#     or c == "garb" and ((k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2)) \
#     or   c == "sharq" and ((k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2))\
#     or  (c == "janub" and ((k1==1 and k2==1) or (k1==0 and k2==0))):
#     print(" 'shimol' ga qarab turibdi ")
# elif (c == "shimol" and ((k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2)))\
#     or (c == "janub" and ((k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2)))\
#     or  (c == "garb" and ((k1==1 and k2==0) or (k1==0 and k2==1)or (k1 == 2 and k2 == 2)))\
#     or (c == "sharq" and ((k1 == 0 and k2 == 0) or (k1 == 1 and k2 == 1))):
#     print(" 'G'arb' ga qarab turibdi ")
# elif (c == "shimol" and ((k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2)))\
#     or (c == "janub" and ((k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2)))\
#     or (c == "garb" and ((k1 == 1 and k2 == 1) or (k1 == 0 and k2 == 0)))\
#     or  (c == "sharq" and ((k1==1 and k2==0) or (k1==0 and k2==1)or (k1 == 2 and k2 == 2))):
#     print(" 'sharq' ga qarab turibdi ")
# elif (c == "shimol" and ((k1 == 0 and k2 == 0) or (k1 == 1 and k2 == 1)))\
#     or  (c == "janub" and ((k1==1 and k2==0) or (k1==0 and k2==1)or (k1 == 2 and k2 == 2)))\
#     or (c == "garb" and ((k1 == 2 and k2 == 0) or (k1 == 0 and k2 == 2)))\
#     or  (c == "sharq" and ((k1 == 2 and k2 == 1) or (k1 == 1 and k2 == 2))):
#     print(" 'Janub' ga qarab turibdi ")
# else:
#     print("Notogri kamanda kiritildi")

# Uyga vazifa. 1 dan 1 000 000 gacha son kiritiladi shuni soz orqali ifodalash

a = int(input("Sonni kiriting - "))
yuzm = a//100000
onm = a % 100000//1000 - a % 10000//1000
birm = a % 10000//1000
yuzlik = a % 1000 // 100
onlik = a % 100 - a % 10
birlik = a % 10

if birlik == 1 or yuzlik == 1 or birm == 1 or yuzm == 1:
    birlik = "bir" ; yuzlik ="bir"; birm = "bir" ; yuzm = "bir"
if birlik == 2 or yuzlik == 2 or birm == 2:
    birlik = "ikki" ; yuzlik ="ikki"; birm = "ikki"
print(yuzm, "yuz ming", onm, birm, "ming", yuzlik, "yuz", onlik, birlik)


































