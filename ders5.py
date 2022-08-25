##pass continue break yapıları

#Örn1
#5'ten 9'a kadar olan sayılarda 7 hariç diğer sayıları gösterin 

x=5
while x<=9:
    if x != 7:
        print(x)
    x += 1

x=5
while x<=9:
    if x == 7:
        x += 1
        continue
    print(x)
    x += 1

#Örn 2
#1'den 9'e kadar olan sayılardan 4 ve 5 dışındakileri toplayarak ekrana toplam sonucu yazdırın
x=1
toplam = 0
while x<8:
    if x == 4 or x ==5:
        x += 1
        continue
    toplam += x
    x += 1
print(toplam)

#Örn 3
#3'ten 9'a kadar olan sayılarda 4 ve 6 dışındakilerin birbirileriyle çarpımı nedir?
x=3
carpim = 1
while x<9:
    if x == 4 or x ==5:
        x += 1
        continue
    carpim *= x
    x += 1
print(carpim)

#Örn 4
#Kullanıcı 0 girene kadar girilen değeri ekranda yazan programı yazınız
x = int(input('Sayı giriniz: '))
if x != 0:
    print(x)
else:
    print('0 girmeyiniz') 

"""
while True:
    a= int(input('Sayı giriniz: '))
    if a == 0:
        break
    print(a)
"""

#Örn 5
#Kullanıcı tarafından 8 girilene kadar girilen tüm sayıları toplatınız. Toplam sonucu ekranda yazdırın
toplam = 0
while True:     
    x= int(input('Sayı giriniz: '))
    if x == 8:
        break
    toplam =toplam  + x
print(toplam)

#Pass komutu 
k=2
while k<2:
    pass