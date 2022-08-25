##iç içe if yapısı 
#Soru 1
#Verilen sayılardan 14 ile bölünebilen ve 30 dan büuük sayı ise "evet" yazın
a=int(input("Sayı giriniz:  "))
if a>30:
    if a % 14 == 0:
        print("Evet")

#Soru 2
#kullanıcının girdiği sayı çift ve 20den küçükse "evet" yazdırın
c=int(input("Sayı giriniz:  "))
if a<20:
    if a % 2 == 0:
        print("Evet")

##Or ve ya and ile if'le kodlama
# Soru 3
# Girilen sayılardan 8 ile bölünebilen veya 12den büyük sayılar için "evet" yazdırın
b=int(input("Sayı giriniz:  "))
if b % 8 == 0 or b>12:
    print("evet")

##Döngüler##
#While yapısı
#Soru 4
#1'den 9'a kadar sayıları yazıdırın
x =0 
while x<=9:
    print(x) #eğer x = X+1 yazmazsak devamlı 0 yazmaya devam eder bunu durdurmak için x = x+1 ifadesini koyduk
    x = x +1
print('bitti')

#Soru 5
#1'den35ye kadar 6'ya bölünen sayılar
x =0 
while x<=35:
    if x % 6 ==0: 
        print(x) #eğer x = X+1 yazmazsak devamlı 0 yazmaya devam eder bunu durdurmak için x = x+1 ifadesini koyduk
    x = x +1
print('bitti')

#Soru 6
#1'den 6'a kadar olan sayıları (3. hariç) ekranda gösterin
x =0
while x<=6:
    if x!=3: 
        print(x) #eğer x = X+1 yazmazsak devamlı 0 yazmaya devam eder bunu durdurmak için x = x+1 ifadesini koyduk
    x = x +1
print('bitti')