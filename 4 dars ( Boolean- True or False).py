# Mavzu: Boolean (to'g'ri yoki xato amali(True or False))

##MASALA:  Tomoni a va b bolgan togri to'rtburchakka tomoni c bolgan kvadratdan nechtasi joylashtiraolish masalasi
# c = int(input('c-')) ; a = int(input('c dan katta son kiriting: a-')); b = int(input('c dan katta son kiriting: b-'))
# n = a//c * b//c ; y = a*b-n*c*c; print(n,'ta joylashadi',f'{y}m^2 - shunday qismi ortib qoladi')

##MASALA: tomonlari a,b,c bolgan paralipipedga tomoni x bolgan kubikdan nechta sigadi
# x = int(input('x-')) ; a = int(input('x dan katta son kiriting: a-')); b = int(input('x dan katta son kiriting: b-')); c=int(input('x dan katta son kiriting z-'))
# n = a//x * b//x * c//x; y = a*b*c - n*pow(x,3); print(f'{n} ta joylashadi {y} m^3 hajm ortib qoladi')

# #MASALA: Ikkita son kiritasiz bittasi juft bittasi toq bolsa - true bolmasa false
# a = int(input('a sonni kiriting-'));b = int(input('b sonni kiriting-'))
# print((a%2==0 and b%2==1) or (a%2==1 and b%2==0) );

#MASALA: 4 ta sonnii 5 chi son qoshmasdan o'rnini almashtiruvchi dastur
# a = int(input('a-')); b = int(input('b-')); c = int(input('c-')); d = int(input('d-'))
# a = a+b+c+d; b = a-b-c-d; c = a-b-d-c; d = a-b-c-d; a = a-b-c-d;
# print(f'Natija a-{a}', f'b-{b}', 'c-',c, 'd-',d)

#MASALA:3 ta son kiritasiz va osha sonlarning o'rtasidagi sonni topish dasturi
# a, b, c = map(int, input('Sonlarni kiriting (faqat probel bilan) \na-, b-, c- '). split())
# x = ((a>b>c) * b) + ((b>a>c) * a) + ((b>c>a) * c) + ((c>b>a) * b) + ((a>c>b) * c) + ((c>a>b) * a)
# print(f'Kiritilgan sonlar ichida ortancha qiymat - {x}')

# MASALA: N ta son berilgan shu sonalrning ichid eng kichik musbat sonni topish kerak
#ishlab bilmadim

#UYGA VAZIFA
# # 1-masala. 1 dan 7 gacha sonlar berilgan xafta kunlariga mos ravishda berilgan .Kirtilgan songa mos ravishda qaysi kunliki topilsin
# a  = int(input('1 dan 7 gacha bolgan son kirting K- '))
# x = (a==1)*'Dushanba'+(a==2)*'Seshanba'+(a==3)*'Chorshanba'+(a==4)*'Payshanba'+(a==5)*'Juma'
# y = (a==6)*'Shanba'+(a==7)*'Yakshanba'+(a>7 or a<0)*'Xato raqam'
# print(x+y)

# # 4 masala. Oy raqami berilgan. shu oyda nechta kun borligini topuvchi dastur tuzing
# a  = int(input('Nechanchi oyligini kirting K- '))
# x = (a==1)*'Yanvar 31 kun'+(a==2)*'Fevral 28 yoki 29 kun'+(a==3)*'Mart 31 kun'+(a==4)*'Aprel 30 kun'+(a==5)*'May 31 kun'
# y = (a==6)*'Iyun 30 kun'+(a==7)*'Iyul 31 kun'+(a==8)*'Avgust 31 kun'+(a==9)*'Sentyabr 30 kun'+(a>12 or a<0)*'Xato raqam'
# z = (a==10)*'Oktyabr 31 kun'+(a==11)*'Noyabr 30 kun'+(a==12)*'Dekabr 31 kun'
# print(x+y+z)

# # 5 masala A va B sonlari berilgan shu sonlar ustida Qoshish, ayirish , bolish va kopaytirish amallarini bajaruvchi dastur
# a  = int(input('A- ')); b = int(input('B- ')); x = input('Qanday amal bajarish kerak-')
# Natija = (a+b)*(x=='qoshsish') + (abs(a-b))*(x == 'ayirish') + (a*b)*(x=='kopaytirish')+ (a/b)*( x== 'bolish' and b != 0 and a>b) + (b/a)*( x== 'bolish' and a != 0 and a<b)
# print(Natija)

# #10 masala; Robot xolatini aniqlovchi dastur
# print("Kamanda: 0-oldinga, 1-chapga, 2-ongga")
# k = int(input('Kamanda bering- ')); y = input("Yo'nalishi(faqat 4 ta tomonni yozing) - ")
# x = (k==0 and y =='janub')*'janubga qarab turibdi'+(k==0 and y == 'shimol')*'shimolga qarab turibdi'+(k==0 and y == 'garb')*'garbga qarab turibdi'+(k==0 and y == 'sharq')*'sharqga qarab turibdi'
# Y = (k==1 and y =='janub')*'Sharqqa qarab turibdi'+(k==1 and y =='shimol')*'Garbqa qarab turibdi'+(k==1 and y =='garb' )*'Janubqa qarab turibdi'+(k==1 and y =='sharq' )*'Shimolqa qarab turibdi'
# z = (k==2 and y == 'janub')*'Garbga qarab turibdi'+(k==2 and y == 'shimol')*'Sharqga qarab turibdi'+(k==2 and y == 'garb')*'Shimolga qarab turibdi'+(k==2 and y == 'sharq')*'januba qarab turibdi'
# print(x+Y+z)

# # Rostlikka tekshirish degani berilgan shart bajarilsa - True chiqishi agar bajarilmasa - False chiqishini tushinish kerak
# # 12-masala:A,B va C sonlari berilgan:Jumlani rostlikka tekshiring: uchala son ham musbat
# a = int(input('A- ')); b = int(input('B- ')); c = int(input('C- '))
# x = (a>0)*(b>0)*(c>0)*'True' + (a<0 or b<0 or c<0)*'False'; print(x)
#
# # 13 masala. Bu masalada kamida bittasi musbat bolsa natija rost chiqishi kk
# while True:
#     try:
#         a = int(input('A- '))
#         b = int(input('B- '))
#         c = int(input('C- '))
#         x = (a > 0 or b > 0 or c > 0) * 'True' + (a < 0 and b < 0 and c < 0) * 'False'
#         print(x)
#     except :
#         print("faqat son kirting")
#     cont = input("Agar davom etmoqchi bo'sangiz 'enter' bosing, tugatmoqchi bo'lsangiz 'exit' deb yozing")
#     if cont == " exit " :
#        break

# # 14 masala Endi faqat bittasi musbat qolgan 2 tasi manfiy bolsa True bolmasa False chiqishi kk
# while True:
#     try:
#         a = int(input('A- '))
#         b = int(input('B- '))
#         c = int(input('C- '))
#         x = (a > 0 and b < 0 and c < 0) or (a< 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c < 0)
#         print(x)
#     except:
#         print("faqat son kirting")
#     cont = input("Agar davom etmoqchi bo'sangiz 'enter' bosing, tugatmoqchi bo'lsangiz 'exit' deb yozing")
#     if cont == " exit ":
#         break

# # 20 masala.Uch xonali son berilgan uni rostlikka tekshirish.Sonni raqamlari xar xil bolishi kerak,
# a = int(input("uch xonali son kiriting - "))
# x = (a//100) != (a%100//10) != (a%10); print(x)

# # 21 masala. Endi shu sonlar ketma ket osuvchi bolib joylashishi kerak
# a = int(input("uch xonali son kiriting - "))
# x = (a//100) < (a%100//10) < (a%10); print(x)

# #22 masala Endi Shu sonlar ketma ket osuvchi yoki kamayuvchi bolib joylashishi kerak
# a = int(input("uch xonali son kiriting - "))
# x = ((a//100) < (a%100//10) < (a%10)) or ((a//100) > (a%100//10) > (a%10)); print(x)

# #23 masala Endi Berilgan sonni ongdan ham chapdan ham oqisangiz bir xil bolish kerak
# a = int(input("uch xonali son kiriting - "))
# x = ((a//100)==(a%10)) or ((a//100) == (a%100//10) == (a%10)); print(x)

# # 28 masala. (x,y) nuqta berilgan shu nuqta koordinatalar oqida birinchi va uchinchi choragida yotishini topish
# x = int(input("x kiriting - ")); y = int(input("y kiriting - "))
# natija = (x>0 and y>0)* ' Birinchi chorakda ' + (x>0 and y<0)* ' Ikkinchi chorakda ' + (x<=0 and y == int(y))* 'Bu nuqta 1 va 3- choraklarda yotmaydi '
# print(natija)

# #29 masala.(x,y) nuqta berilgan. Chap yuqori choqqqis (x1,y1) nuqtada va o'ng pastki qismi (x2,y2) nuqtalarda bolgan tomonlari koordinata oqlariga parellel bolgna togri tortburchak ichida yotzdi
# #Jumlani rostlikga tekshiring
# x, y = map(int,input("x va y ni kiriting- ").split()); x1, y1 = map(int,input("x1 va y1 ni kiriting- ").split()); x2, y2 = map(int,input("x2 va y2 ni kiriting- ").split())
# natija = (x2<x<x1 and y2<y<y1); print(natija)

# # 31 masala tomonlari a, b va c bolgan uchberchak berilgan uni rostlikka tekshiring.teng tomonli uchburchak bolsa true chiqishi kk
# a = int(input("a tomonini kiriting - ")); b = int(input("b tomonini kiriting - ")); c = int(input("c tomonini kiriting - "))
# natija = (a==b and (a+b)>c) or (a==c and (a+c)>b) or (c==b and (c+b)>a); print(natija)

# # 32 masala.tomonlari a, b va c bolgan uchberchak berilgan uni rostlikka tekshiring. To'g'ri burchakli uchburchak bolsa true chiqishi kk
# from math import sqrt
# a = int(input("a tomonini kiriting - ")); b = int(input("b tomonini kiriting - "));c = int(input("c tomonini kiriting - "))
# natija = (a == sqrt(b**2+c**2)) or (b == sqrt(a**2+c**2)) or (c==sqrt(a**2+b**2)); print(natija)

# # 34 masala. Shaxmat doskasining (x, y) koordinatalari berilgan.(1-8 orqaliqida yotuvchi butun sonlar). Shaxmatning chap paski qismi (1,1) koordinatasi qoraligidan xisoblanib
# #            siz kiritgan koordinaa agar oq katagi bolsa true aks xolda false chiqishi kk
# x = int(input(" x ni kiriting - ")); y = int(input(" y ni kiriting - "))
# natija = x!=y and ((x+y)%2) == 1 ; print(natija)

# # 35 masala endi.(x1,y1) va (x2,y2) koordinatalar berilgan agar ular bir xil rangda bolsa true bolmasa false chiqsin
# x1 = int(input(" x1 ni kiriting - ")); y1 = int(input(" y1 ni kiriting - "));x2 = int(input(" x2 ni kiriting - ")); y2 = int(input(" y2 ni kiriting - "))
# natija = ((x1+y1)%2 == 0 and (x2+y2)%2 == 0) or ((x1+y1)%2 == 1 and (x2+y2)%2 == 1) ; print(natija)

# # 36 masala endi.(x1,y1) va (x2,y2) koordinatalar berilgan.Ruh(to'ra) otini kataklarda qoida bo'yicha yurishi togri  bolsa true bolmasa false chiqsin
# x1 = int(input(" x1 ni kiriting - ")); y1 = int(input(" y1 ni kiriting - "));x2 = int(input(" x2 ni kiriting - ")); y2 = int(input(" y2 ni kiriting - "))
# natija = (x1==x2 and y1>y2) or (x1==x2 and y2>y1) or (x1>x2 and y1==y2) or (x1<x2 and y1==y2) ; print(natija)

# # 37 masala. Bu masalada shoxni qoidaga mos ravishda yurishini tekshiramiz
# x1 = int(input(" x1 ni kiriting - ")); y1 = int(input(" y1 ni kiriting - "));x2 = int(input(" x2 ni kiriting - ")); y2 = int(input(" y2 ni kiriting - "))
# natija = natija = (x1 - x2 >= -1) and (x1 - x2 <= 1) and (y1 - y2 >= -1) and (y1 - y2 <= 1) and not (x1 == x2 and y1 == y2); print(natija)

# # 38 masala. Bu masalada Filni qoidaga mos ravishda yurishini tekshiramiz
# x1 = int(input(" x1 ni kiriting - ")); y1 = int(input(" y1 ni kiriting - "));x2 = int(input(" x2 ni kiriting - ")); y2 = int(input(" y2 ni kiriting - "))
# natija = natija = abs(x1-x2)==abs(y1-y2) and not (x1 == x2 and y1 == y2); print(natija)

# # 39 masala. Bu masalada Farzinni qoidaga mos ravishda yurishini tekshiramiz
# x1 = int(input(" x1 ni kiriting - ")); y1 = int(input(" y1 ni kiriting - "));x2 = int(input(" x2 ni kiriting - ")); y2 = int(input(" y2 ni kiriting - "))
# natija = ( (x1==x2 and 0<= abs(y1-y2) <=7 and y1!=y2) or (y1==y2 and 0<=abs(x1-x2)<=7 and x1!=x2) ) or (abs(x1-x2)==abs(y1-y2) and not (x1 == x2 and y1 == y2))
# print(natija)

# 40 masala. Bu masalada OTni qoidaga mos ravishda yurishini tekshiramiz
x1 = int(input(" x1 ni kiriting - ")); y1 = int(input(" y1 ni kiriting - "));x2 = int(input(" x2 ni kiriting - ")); y2 = int(input(" y2 ni kiriting - "))
natija = (abs(x1-x2)==2* abs(y1-y2) or 2* abs(x1-x2)==abs(y1-y2) and not (x1 == x2 and y1 == y2))
print(natija)

# G'ALABA   SOAT 00 :05 VA NIHOYAT TUGATDIM....

