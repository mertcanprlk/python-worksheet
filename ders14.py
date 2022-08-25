#SPLİT METODU#

#Split fonksiyonu çıktı olarak liste verir
#Argümansız kullanıldığında,boşlıklardan stringi ayırır

k="Bugün hava çok güzel."
print(k.split())

m="Ayva, armut, üzüm, kiraz"
print(m.split())

m="Ayva, armut, üzüm, kiraz" 
print(m.split(",")) #içine koyduğumuz değeri liste içerisinde göstermez

m="Ayva, armut, üzüm, kiraz" 
print(m.split("a")) #küçük a'ların hiçbirini göstermedi

m="Ayva, armut, üzüm, kiraz" 
print(m.split("a",1)) #parametre 1 olarak belirtildiği için küçük a harfinden sadece 1 tanesini göstermez

m="Ayva, armut, üzüm, kiraz" 
print(m.split(",",1)) #Böyle yaparak ayvayı ayrı diğer meyveleri ayrı olarak gösterebiliriz böylelikle liste içerisinde de bir ayrım yapabiliriz

#REPLACE FONKSİYONU#

k="Bugün hava çok güzel."
print(k.replace("hava","gün")) #Hava yerine gün yazdık

k="Bugün hava çok güzel."
print(k.replace("h","k")) #küçük h harfi yerine küçük k harfi yazdırdık

k="Bugün hava çok güzel."
print(k.replace("ü","i",1)) #ilk ü harfini i yapar diğerlerini yapmaz

#KARAKTERLERİ AYIRMA#
k="Bugün hava çok güzel" 
print(k[-5:]) #Cümledeki güzel kelimesini bu kodla alabiliriz

k="Bugün hava çok güzel"
print(k[:5]) #Cümledeki bugün kelimesini bu kodla alabiliriz

# Not: len() komutu
"""
print(len(k)) #k cümlesi kaç harften oluşuyor sorusunu yanıtlar len() komutu
"""

# Soru1
# k="Bugün hava çok güzel" stringinde ortadaki iki karakteri gösterin

# 1. yol
k="Bugün hava çok güzel"
print(k[9:11]) 

#2. yol
ortadaki= k[len(k)//2-1:len(k)//2+1]
print(ortadaki)

#Soru2
# B201306004 öğrenci nosunda ikinci ve üçüncü karakter giriş yılını gösterdiğine göre bu öğrencinin giriş yılını bulunuz
a="B201306004"
print(a[1:3])

#Soru3
# "B" ile başlayan,2015 girişli, 1306004.,sıradaki öğrenci nosu nedir?

a="B" + "15" + "1306004"
print(a)

#RASTGELE SAYI ÜRETİMİ#
import random
print(random.randint(0,9)) #0'dan 9'a kadar (9da dahil) rakamlar üretir

#soru 1
#1'den 20'e kadar olan tamsayılardan 5 tane üreterek bunları bir liste içinde yazdırın
a=[]
for k in range(5):
    a.append(random.randint(1,20))
print(a)





