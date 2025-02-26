# IF ni davomi

# # 1 masala.1-7 gacha bo'lgan butun sonlar berilgan. Kiritilgan songa mos ravishda hafta kunlarini
# #          so'zda ifodalovchi programma tuzilsin. (1-Dushanba, 2-Chorshanba,...h.k)
# a = int(input("a - "))
# if 1 <= a <= 7:
#     if a == 1:
#         print("Dushanba")
#     elif a == 2:
#         print("Seshanba")
#     elif a == 3:
#         print("Chorshanba")
#     elif a == 4:
#         print("Payshanba")
#     elif a == 5:
#         print("Juma")
#     elif a == 6:
#         print("shanba")
#     else:
#         print("Yakshanba")
# else:
#     print(" 1 dan 7 gacha son kiriting")

# # 3 masala:Oy raqamini berilgan. Kiritilgan oy qaysi faslga tegishli ekanligini chiqaruvchi programma tuzilsin. (Masalan: 2 chi oy, "qish")
# a = int(input("a - "))

# if 1<=a<=12:
#     if a == 1 or a == 2 or a == 12:
#         print("Bu oy 'Qish' faslida")
#     elif a == 3 or a == 4 or a == 5:
#         print("Bu oy 'Bahor' faslida")
#     elif a == 6 or a == 7 or a == 8:
#         print("Bu oy 'Yoz' faslida")
#     else:
#         print("Bu oy 'Kuz' faslida")
# else:
#     print(" 1 dan 12 gacha son kiriting")

# # 4 masala: Oy raqami berilgan. Shu oyda nechta kun borligini aniqlovchi programma tuzilsin.
# a = int(input("a - "))

# if 1<=a<=12:
#     if a == 1 or a == 12 or a == 3 or a == 5\
#             or a == 7 or a == 8 or a == 10:
#         print("Bu oyda '31' kun bor")
#     elif a == 6 or a == 4 or a == 9 or a == 11:
#         print("Bu oyda '30' kun bor ")
#     else:
#         print("Bu oyda '28 yoki 29 ' kun bor ")
# else:
#     print(" 1 dan 12 gacha son kiriting")

# # 5 masala: Ikki son ustida 4 ta amal bajaruvchi kalkulyator

# a = int(input("a- "))
# b = int(input("b- "))
# amal =str(input("amalni kiriting - "))
# if amal == str("qoshish"):
#     print(a + b)
# elif amal == str("ayirish"):
#     print(a-b)
# elif amal == "kopaytirish" :
#     print(a*b)
# elif amal == "bolish":
#     print(a/b)
# else :
#     print("xato")

# # 6 masala. Uzinlik birliklari quyidagi tartibda berilgan. 1-desimetr, 2-kilometr, 3-metr, 4-millimeter, 5-santimetr.
# #           Uzunlik birligini bildiruvchi son berilgan (1-5 oraliqda) va shu birlikdagi kesma uzunligi

# a = int(input("a- "))
# if 1<=a<=5:
#     if a == 1:
#         print(" 1 detsimetr = 0.1 m")
#     elif a == 2:
#         print(" 1 kilimetr = 1000 m ")
#     elif a == 3:
#         print(" 1 m = 1 m ")
#     elif a == 4:
#         print(" 1 millimetr = 0.0001 m ")
#     else:
#         print(" 1 santimetr = 0.001 ")
# else:
#     print(" 1 dan 5 gacha son kiriting")
#

# # 8 masala.Sanani bildiruvchi ikkita butun son berilgan D (kun) va M (oy). (Kabisa bo`lmagan yil sanasi kiritiladi)
# #  Berilgan sanani ifodalovchi programma tuzilsin. Kabisa yilida 366 kun, kabisa bo'lmagan yilda 365 kun bor bo'ladi.

# d = int(input("Kunni kiriting - ")); m = int(input("Oyni kiriting - "))
# if 0<=d<=31 and 1<=m<=12:
#     if m == 1:
#         print(f" {d} - yanvar " )
#     elif m == 2 and d <=28 :
#         print (f" {d} - fevral ")
#     elif m == 3:
#         print (f" {d} - Mart ")
#     elif m == 4 and d<=30:
#         print (f" {d} - Aprel ")
#     elif m == 5:
#         print (f" {d} - May ")
#     elif m == 6 and d!=31 :
#         print (f" {d} - Iyun ")
#     elif m == 7:
#         print (f" {d} - Iyul ")
#     elif m == 8:
#         print (f" {d} - Avgust ")
#     elif m == 9 and d!=31 :
#         print (f" {d} - Sentyabr ")
#     elif m == 10:
#         print (f" {d} - Oktiyabr ")
#     elif m == 11 and d!=31 :
#         print (f" {d} - Nayabr ")
#     elif m == 12:
#         print (f" {d} - Dekabr ")
# else:
#     print("Notog'ri sana kiritildi")

# # 10 masala. Robot faqat to`rtta tomonga ko`cha oladi ("s"-shimol, "j"-janub, "q"-sharq, "g"-g'arb) va uchta raqamli kamanda: 0-harakni davom ettir, 1-chapga buril,
# # 2-o`ngga buril.Y - robot yo`nalishi va K -kamanda berilgan. Berilgan kamanda bajarilgandan keying robot holatini aniqlovchi programma tuzilsin.
# print("Kamanda: 0-oldinga, 1-chapga, 2-ongga")

# k = int(input('Kamanda bering- ')); y = input("Yo'nalishi(faqat 4 ta tomonni yozing) - ")
# if 0<=k<=2 and (y=="shimol" or y =="janub" or y == "garb" or y == "sharq"):
#     if k == 0 and y=="shimol" :
#         print("Robot shimolga qarba turibdi")
#     elif k == 0 and y=="janub" :
#         print("Robot janubga qarba turibdi")
#     elif k == 0 and y=="garb" :
#         print("Robot garbga qarba turibdi")
#     elif k == 0 and y=="sharq" :
#         print("Robot sharqga qarba turibdi")
#     elif k == 1 and y=="shimol" :
#         print("Robot G'arbga qarba turibdi")
#     elif k == 1 and y=="janub" :
#         print("Robot sharqga qarba turibdi")
#     elif k == 1 and y=="garb" :
#         print("Robot januba qarba turibdi")
#     elif k == 1 and y=="sharq" :
#         print("Robot Shimolga qarba turibdi")
#     elif k == 2 and y=="shimol" :
#         print("Robot sharqga qarba turibdi")
#     elif k == 2 and y=="janub" :
#         print("Robot G'arbga qarba turibdi")
#     elif k == 2 and y=="sharq" :
#         print("Robot Janubga qarba turibdi")
#     elif k == 2 and y=="G'arb" :
#         print("Robot Shimolga qarba turibdi")
# else:
#     print("Notog'ri kamanda yoki tomonni kirittingi")

# # 12 masala. Doiraning elementlari quyidagi tartibda nomerlangan. 1-radius R, 2-diametr D = 2-R, 3-uzunligi L = 2-π-R,
# #           4-doiraning yuzasi S = π-R². Shu elementlardan bittasi berilganda qolganlarini topuvchi programma tuzilsin. π = 3.14

# b = str(input(" Berilgan parametrini (radius, yuza, diametr, uzunlik) kiriting - "))
# q = float(input(" Qiymatini kiriting - "))
# pi = 3.14
# if q >= 0 and (b=="radius" or b=="yuza" or b=="diametr" or b=="uzunlik"):
#     if b=="radius" :
#         d = 2*q ; l = 2*pi*q ; s = pi*q*q
#         print(f"diametri - {d}, uzunligi - {l}, Yuzasi - {s}")
#     elif b=="diametr":
#         r = q/2 ; l = 2*pi*r ; s = pi*r*r
#         print(f"radiusi - {r}, uzunligi - {l}, Yuzasi - {s}")
#     elif b=="uzunlik":
#         r = q/(2*pi) ; d = 2*r ; s = pi*r*r
#         print(f"radiusi - {r}, diametri -{d}, Yuzasi - {s}")
#     elif b=="yuza":
#         r = (q/pi)**1/2 ; d = 2*r ; l = 2*pi*r
#         print(f"radiusi - {r},diametri - {d} , uzunligi - {l}")
# else:
#     print(" Biron nimani notog'ri kirittingiz")


# 15 masala. O'yin kartasi turlari berilgan 1-g'isht, 2-olma, 3-chillak, 4-qarg'a. 10 lik kartadan katta kartalar quyidagi
#  qiymatlarni o`zlashtirgan: 11-valet, 12-dama, 13-qirol, 14-tuz. Ikkita butun son berilgan N-karta qiymati (6≤ N ≤14)
#  M-karta turi (1≤ M ≤4) kiritilganda karta nomlarini (masalan: "olti qarg`a") chiqarib beruvchi programma tuzilsin.

# n = int(input("karta qiymatini kiriting (6≤ N ≤14) N - ")) ;m = int(input("karta turi (1≤ M ≤4) M - "))
# if 6<=n<=14 and 1<=m<=4:
#     if  n==6 :
#         if  m == 1:
#             print("olti g'isht")
#         elif m==2:
#             print("olti olma")
#         elif  m==3:
#             print("olti chillak")
#         else:
#             print("olti qarg'a")
#     elif n==7 :
#         if m==1:
#             print("yetti g'isht")
#         elif  m==2:
#             print("yetti olma")
#         elif m==3:
#             print("yetti chillak")
#         else:
#             print("yetti qarg'a")
#     elif n==8 :
#         if m==1:
#             print("sakkiz g'isht")
#         elif m==2:
#             print("sakkiz  olma")
#         elif  m==3:
#             print("sakkiz  chillak")
#         else:
#             print("sakkiz  qarg'a")
#     elif n==9 :
#         if m==1:
#             print("toqqiz g'isht")
#         elif  m==2:
#             print("toqqiz  olma")
#         elif  m==3:
#             print("toqqiz  chillak")
#         else:
#             print("toqqiz  qarg'a")
#     elif n==10 :
#         if m==1:
#             print("o'n g'isht")
#         elif  m==2:
#             print("o'n  olma")
#         elif  m==3:
#             print("o'n  chillak")
#         else:
#             print("o'n  qarg'a")
#     elif n==11:
#         if m==1:
#             print("valet g'isht")
#         elif m==2:
#             print("valet  olma")
#         elif  m==3:
#             print("valet  chillak")
#         else:
#             print("valet  qarg'a")
#     elif n==12 :
#         if m==1:
#             print("dama g'isht")
#         elif n==6 and m==2:
#             print("dama  olma")
#         elif n==6 and m==3:
#             print("dama  chillak")
#         else:
#             print("dama  qarg'a")
#     elif n==13 :
#         if m==1:
#             print("qirol g'isht")
#         elif  m==2:
#             print("qirol  olma")
#         elif m==3:
#             print("qirol  chillak")
#         else:
#             print("qirol  qarg'a")
#     elif n==14:
#         if m==1:
#             print("tuz g'isht")
#         if  m==2:
#             print("tuz  olma")
#         elif m==3:
#             print("tuz  chillak")
#         else:
#             print("tuz  qarg'a")
# else:
#     print("Notog'ri sonlar kiritildi")


# # 18 masala. 100-999 gacha oraliqdagi sonlarni so'zlarda ifodalovchi programma tuzilsin. (masalan: 123-"bir yuz yigirma uch").
#
# a = int(input(" Sonni kiriting - "))
# yuzlik = a//100
# onlik = a%100 - a%10
# birlik = a%10
# if 100<=a<=999:
#     if yuzlik == 1:
#         print("bir yuz",end=" ")
#     elif yuzlik == 2:
#         print("ikki yuz ", end="")
#     elif yuzlik == 3:
#         print("uch yuz ", end="")
#     elif yuzlik == 4:
#         print("tort yuz ", end="")
#     elif yuzlik == 5:
#         print("besh yuz ", end="")
#     elif yuzlik == 6:
#         print("Olti yuz ", end="")
#     elif yuzlik ==7 :
#         print("yetti yuz ", end="")
#     elif yuzlik == 8:
#         print("sakkiz yuz ", end="")
#     elif yuzlik == 9:
#         print("toqqiz yuz ", end="")
#     if onlik == 10:
#         print("o'n", end=" ")
#     elif onlik == 20:
#         print("yigirma", end=" ")
#     elif onlik == 30:
#         print("o'ttiz", end=" ")
#     elif onlik == 40:
#         print("qirq", end=" ")
#     elif onlik == 50:
#         print("ellik", end=" ")
#     elif onlik == 60:
#         print("oltmish", end=" ")
#     elif onlik == 70:
#         print("yetmish", end=" ")
#     elif onlik == 80:
#         print("sakson", end=" ")
#     elif onlik == 90:
#         print("to'qson", end=" ")
#     if birlik == 1:
#         print("bir")
#     elif birlik == 2:
#         print("ikki")
#     elif birlik == 3:
#         print("uch")
#     elif birlik == 4:
#         print("besh")
#     elif birlik == 6:
#         print("olti")
#     elif birlik == 7:
#         print("yetti")
#     elif birlik == 8:
#         print("sakkiz")
#     elif birlik == 9:
#         print("to'qqiz")
# else:
#     print("100-999 gacha oraliqdagi son kiriting")

# # 19 maasala. Sharq kalendarida 60 yillik davr qabul qilingan. Yil muchali 5 ta rang (yashil, qizil, sariq, oq va qora) va 12 ta hayvon
# #             (sichqon, sigir, yo'lbars, quyon, ajdar, ilon, ot, qo`y, maymun, tovuq, it va to`ngizlardan) nomlaring kombinatsiyasidan kelib chiqadi.
# #            Yilning raqamiga qarab uning muchalini aniqlovchi programma tuzilsin. 1984-davr boshi: "Yashil sichqon yili”.
#
# a = int(input("Yilni kiriting - "))
# x = a - 1983 # Kiritilgan yilni yil boshidan ayramiz
# muchal = x % 5
# yili =  x % 12
# if a >= 1983:
#     if muchal == 1:
#         print(" yashil",end=" ")
#     elif muchal == 2:
#         print(" Qizil",end=" ")
#     elif muchal == 3:
#         print("Sariq",end=" ")
#     elif muchal == 4:
#         print("Oq",end=" ")
#     elif muchal == 0:
#         print("Qora",end=" ")
#     if yili == 1:
#         print("sichqon yili")
#     elif yili == 2:
#         print("sigir yili")
#     elif yili == 3:
#         print("yo'lbars yili")
#     elif yili == 4:
#         print("quyon yili")
#     elif yili == 5:
#         print("ajdar yili")
#     elif yili == 6:
#         print("ilon yili")
#     elif yili == 7:
#         print("ot yili")
#     elif yili == 8:
#         print("qo'y yili")
#     elif yili == 9:
#         print("maymun yili")
#     elif yili == 10:
#         print("tovuq yili")
#     elif yili == 11:
#         print("it yili")
#     elif yili == 0:
#         print("tong'iz yili")
# else:
#     print(" Notog'ri yil kiritdingiz")

# # 20 masala.Ikkita burj vaqtlarini aniqlovchi butun son berilgan: D(kun), M(oy). Berilgan sana qaysi burjga kirishini aniqlovchi programma tuzilsin.
# "Qovg'a (20.1-18.2)", "Baliq (19.2-20.3)", "Qo`y (21.3-19.4)", "Buzoq (20.4-20.5)', "Egizaklar (21.5-21.6)", "Qisqichbaqa (22.6-22.7)", "Arslon (23.7-22.8)",
# "Parizod (23.8-22.9)', "Tarozi (23.9-22.10)","Chayon (23.10-22.11)', "O`qotar (23.11-21.12)', "Echki (22.12-19.1)".

d = int(input(" Kunni kiriting - ")); m = int(input(" oyni kiriting - "))
if 1<=m<=12 and 1<=d<=31:
    if (20<=d<=31 and m==1) or (1<=d<=18 and m==2):
        print("Burj- Qavg'a")
    elif (19<=d<=31 and m==2) or (1<=d<=20 and m==3):
        print("Burj- Baliq ")
    elif (21<=d<=31 and m==3) or (1<=d<=19 and m==4):
        print("Burj- Qo'y ")
    elif (20<=d<=30 and m==4) or (1<=d<=20 and m==5):
        print("Burj- Buzoq ")
    elif (21<=d<=31 and m==5) or (1<=d<=21 and m==6):
        print("Burj- Egizaklar ")
    elif (22<=d<=30 and m==6) or (1<=d<=22 and m==7):
        print("Burj- Qisqichbaqa ")
    elif (23<=d<=31 and m==7) or (1<=d<=22 and m==8):
        print("Burj- Arslon ")
    elif (23<=d<=31 and m==8) or (1<=d<=22 and m==9):
        print("Burj- Parizod ")
    elif (23<=d<=30 and m==9) or (1<=d<=22 and m==10):
        print("Burj- Tarozi ")
    elif (23<=d<=31 and m==10) or (1<=d<=22 and m==11):
        print("Burj- Chayon ")
    elif (23<=d<=30 and m==11) or (1<=d<=21 and m==12):
        print("Burj- O'qotar ")
    elif (22<=d<=31 and m==12) or (1<=d<=19 and m==1):
        print("Burj- Echki ")
else:
    print("Noto'g'ri raqam kiritildi")
