#Fonksiyon kullanımı için Lambda metodu 
#Kısa işlem gerektiren fonksiyonlar lambda ile yazılabilir.

"""
fonksiyon_ismi= lambda parametre_adı1, parametre_adı2: geriye dönecek değer
"""

#Örnek
#Verilen sayının karesini alan fonksiyonu klasik yapı ve lambda kullanarak yazınız 
#1. yöntem
from re import M


def kare(x):
    return  x**2

e=kare(2)
print(e)

#2. yöntem
kare2=lambda x: x**2

k=kare2(5)
print(k)

#Soru 1
#Verilen 3 sayının ortalamasını döndüren fonksiyonu lambda ile yazın
ort= lambda x,y,z: (x+y+z)/3

a=ort(9,8,2)
print(a)

#Soru 2
#3x+8y+8xy değerini sonucunu lambda ile döndürün
s= lambda x,y: 3*x+8*(y+x*y)

r=s(9,8)
print(r)

#Soru 3
#Verilen sayı çift ise true değilse false diye lambda ile döndürün
cift= lambda x : x%2==0 

q=cift(5)
print(q)

#Sual 4
#Verilen sayı 50 ile 100 arasında ise true,değilse false diye lambda ile döndürün
aralik= lambda x : 50>x and x<100 

q=aralik(75)
print(q)

#Lambda ile karar yapısının kullanılması#
#fonk_ismi = lambda x,y return1 if sorgu1 else return2

#Soru5
#50 ve 50den büyük not için "geçtin", altı için "kaldın" yazan fonksiyonu lambda ile yazınız 
gk=  lambda x: "geçtin" if x>=50 else "kaldın"
l=gk(5)
print(l)

#Soru 6
#Verilen sayı çiftse iki katını,tekse üç katını döndüren fonksiyonu lambda kullanarak yazınız
ct= lambda x: x*2 if x % 2 == 0 else x*3
o=ct(5)
print(o)

#Soru 7
sepet=["elma","ayva","armut"]
#Kullanıcının yazdığı meyve adı, sepette varsa "var", yoksa "yok" olarak yazan fonksiyonu lambda ile yazınız
ss=lambda x: "var" if x in sepet else "yok"
ee=ss("üzüm")
print(ee)

#Lambda'da çoklu karar
# girilen yaşa göre 0-5 yaşa bebek, 5-15 yaşa çocuk ve üstüne genç olarak yazan fonksiyonu lambda ile yazdırınız
aral=lambda x: "bebe" if 0<x<=5 else "cocuk" if x<15 else "genc"
ee=aral(5)
print(ee)
