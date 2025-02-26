
# # Darsdagi mashq: 2025 yilda istalgan kuningizni kiritish orqali haftaning qaysi kunligini topish.
#
# A = int(input('Yilning qaysidir kunini kiriting Kun - '))
# H  = A % 7
# if H == 6:
#     print(A,'chi kun, haftaning - Dushanba kuni')
# elif H == 0:
#     print(A, 'chi kun, haftaning - Seshanba kuni')
# elif H == 1:
#     print(A, 'chi kun, haftaning - Chorshanba kuni')
# elif H == 2:
#     print(A, 'chi kun, haftaning - Payshanba kuni')
# elif H == 3:
#     print(A, 'chi kun, haftaning - Juma kuni')
# elif H == 4:
#     print(A, 'chi kun, haftaning - Shanba kuni')
# elif H == 5:
#     print(A, 'chi kun, haftaning - Yakshanba kuni')

         # Uyga vazifa:
# # 6- masala; Ikki xonali son berilgan .oldin onliklar keyin birliklar xonasoni chiqaruvchi dastur tuzilsin.
# x  = int(input('Ixtiyoriy ikki xonali son kiriting a-'))
# onlik = x // 10 ; birlik = x % 10 ; print('Onlik raqami',onlik, 'birlik raqimi',birlik)
#
# # 7-masala: ikki xonala sonni raqamlar yig'indisi topilsin
# raqamlar_yigindis = onlik + birlik ; print('Ikki xonali sonning raqamlar yigindisi a =',raqamlar_yigindis )
#
# # 8 masala: Ikki xonali sonning raqamlar o'rnini almashtirish dasturi
# print('Kiritilgan sonni raqamlarini ornini almashtiri',str(birlik)+str(onlik))

#9-masala: uch xonali sonni yuzlik, onlik va birlik o'rinda turgan raqamlarini chiqarish
# A =  int(input('Ixtiyoriy 3 xonali son kiriting A - ' ))
# yuzlik = A // 100 ; onlik = A // 10 % 10 ; birlik = A % 10 ; print('yuzlik qismi -',yuzlik,'onlik -',onlik,'birlik -',birlik)
#
# # 10= masala: 3 xonalali sonni raqamlar yigindisini topish
# raqamlar_yigindisi = yuzlik + onlik + birlik; print('Raqamalar yigindisi -',raqamlar_yigindisi)
#
# # 11 masala: 3 xonali sonni o'rnini alamshtirish
# print('Raqamlari almashgan son -',str(birlik)+str(onlik)+str(yuzlik))

# 24-  masala: Shartli operatorni ishlatmasdan. Agar 1 yanvar dushunba bolsa, Yilning istalgan kunini kiritganda haftaning qaysi kuniligini topish dasturi
# a = int(input('Hafta kunlarini belgilab olamiz:'
#               '\n 1 = Dushanba, 2 = Seshanbq, 3 = Chorshanba\n 4 = Payshanba, 5 = Juma, 6 = Shanba, 0 = Yakshanba'
#               ' \nYilning ixtiyoriy  kunini kiriting - '))
# x = a % 7 ; print('Javobi:',x,' tepaga qarab bilib olishingiz mumkin qaysi kunligini')

# MASALA:1 -usul:Isatlgan sekundni kirgizing,bu dastur shu sekundda necha yil, oy, kun soat minut va sekund bor
# A = int(input('Vaqtni kiriting-'))
# yil = A // (60*60*24*360)
# oy = (A - yil*60*60*24*360)//(60*60*24*30)
# kun = (A - yil*60*60*24*360-oy*60*60*24*30)//(24*3600)
# soat = (A - yil*60*60*24*360-oy*60*60*24*30-kun*24*3600)//3600
# daqiqa = (A - yil*60*60*24*360-oy*60*60*24*30-kun*24*3600-soat*3600)//60
# soniya = A - yil*60*60*24*360-oy*60*60*24*30-kun*24*3600-soat*3600 -daqiqa*60
# print(yil,'yil,',oy,'oy,',kun,'kun,',soat,'soat,',daqiqa,'daqiqa,',soniya,'soniya')
#
# # 2-  usul
# A = int(input('Vaqtni kiriting-'))
# yil = A // (60*60*24*360)
# oy = (A % (60*60*24*360))//(60*60*24*30)
# kun = (A % (60*60*24*30))//(24*3600)
# soat = (A % (24*3600))//3600
# daqiqa = (A % 3600)//60
# soniya = A % 60
# print(yil,'yil,',oy,'oy,',kun,'kun,',soat,'soat,',daqiqa,'daqiqa,',soniya,'soniya')

# Masala: ixtiyoriy 3 ta kiritgan sonni ornini almashtirish dasturi.
# a = int(input('a ni kiriting -')); b = int(input('b ni kiriting -')); c = int(input('c ni kiriting -'))
# a = a + b +c; b = a - b- c ; c = a - b- c; a = a - b -c;
# print('a -',a, 'b -',b, 'c -',c)

# MASALA ; 4 xonali sonning raqamlar yigindisini topish.
# a = int(input('Ixtiyoriy 4 xonali son kiriting - '))
# yigindi = a//1000 + a % 1000//100 + a % 100 //10 + a % 10
# print("Raqamlar yig'indi -",yigindi)

#Masala:Darsdagi arifmetik amalnii bajarish
from math import *
a = int(input('x-')); b = int(input('y-')); z = int(input('z-'))
yigindi = pow((pow(a, 2) - pow(b, 2) + pow(z, 2)), 0.25); print('natija-',yigindi)