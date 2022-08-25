##İNPUT KULLANIMI
##input metodu bir değişkenle kullanılır ve ona değer atar atanan değer stringdir

#Örnek1
#girilen iki saının toplamını ekranda gösterin
"""
k=int(input("Sayı giriniz"))
a=int(input("Sayı giriniz"))
z= k+a 
print(z)
"""

#Örnek2
# k=int(input("Sayı giriniz"))
# a=int(input("Sayı giriniz"))
# e=int(input("Sayı giriniz"))
# z= (k+a+e)
# print(z/3)

#EĞER KOŞULU
#if(true):
# print("selam")
#if yapsındaki koşul true değerini veriyorsa, tab boşluğu bırakılarak altına yazılan kodlar çalışır
""""
if(True):
    print("Slm")

if(False):
    print("nbr")
"""

#Örnek 3
#Girilen sayı 0'dan büyükse ekrana "pozitif" yazıdırn
"""
k=int(input("0'dan farklı sayı giriniz"))
if(k>0):
    print("pozitif")
if(k<0):
    print("negatif")
"""

#Örnek4
#0 ile 100 arasındaki sayılara "not aralık değerinde" diye yazıdırın
"""
k=int(input("sayı giriniz"))
if(0<k<100):
    print("not aralık değerindedir")
"""

#Örnek 5
#0dan büyük sayılara pozitif diğerlerine pozitif değil  yazdırınız.
"""
k=int(input("sayı giriniz"))
if(k>0):
    print("pozitif")
else:
    print("negatif")
"""

#Örnek 6
#girilen şifre "65a8" ise "şifre doğru değilse şifre hatalı" yazdırın
""""
k=int(input("sayı giriniz"))
print(type(k))
if k == "65a8":
    print("şifre doğru")
else:
    print("şifre yanlış")
"""

#Örnek 7
#Vücut kitle endeksini hesaplayınk=int(input("sayı giriniz"))
"""
k=float(input("Boy giriniz"))
e=int(input("Kilo giriniz"))
a=e/(k* k)
if(a>40):
    print("Obezsiniz")
if(a<25):
    print("Zarganasınız")
if(25<a<40):
    print("normalsiniz")
"""

##Metinleri karşılaştırırken büyüklük küçüklükte programı sözlük sırasına bakar

#Örnek 8
#Girilen kelime sözlükte "Kalem" kelimesinden öncesiyse "önce", değilse "sonra" yazdırın
"""
k=input("bir kelime giriniz")
if k<"kalem":
    print("öncedir")
else:
    print("sonradır")
"""

#EL İF YAPISI
# if (koşul):
#     kod1
# elif(koşul2):
#     kod2:
# elif(koşul3):
#     kod3
# else:
#     kod4

# Örnek 9
#Girilen notun hangi sonucu döndürdüğünü yazınız
"""
k=input("0 ila 100 arası sayı giriniz")
k=int(k)
if(k<=49):
    print("zayıf")
elif(50<=k<=69):
    print("orta")
elif(70<=k<=84):
    print("iyi")
else:
    print("pekiyi") 
"""

#Örnek 10
#Yaşı girdiğinizde sonucu ekrana yazdırın
"""
k=input("yaşınızı giriniz")
k=int(k)
if(k<=2):
    print("bebek")
elif(k<=14):
    print("çocuk")
elif(k<=39):
    print("genç")
else:
    print("olgun")
"""

#Örnek11
#geliştirici kullanıcıya kız mı erkek mi ve torunu var mı diye sorabilmektedir kullanıcı da yanlış ise 1 sayısını değilse 0 sayısını girmektedir.
#Bulunacak kişi teyze,amca,büyük anne veya dede olabilir. Bunu kullanıdan aldığı cevaba göre bulan programı yazınız.
a=bool(int(input("kullanıcı kız mı?")))
x=bool(int(input("torunu var mı?")))

if (a==1 and x==1):
    print("büyükanne")
elif (a==1 and x==0):
    print("hala")
elif (a==0 and x==1):
    print("dede")
else:
    print("amca")