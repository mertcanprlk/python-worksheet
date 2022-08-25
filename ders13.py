#map fonksiyonu
#Fonksiyonda bir listenin elemanlarını tek tek döndürerek sonuçlarını yine bir liste içinde kullanıcıya sunan yapıdır.
#Tanımlanan Fonksiyon tek parametreli olmalıdır 

"""
list(map(fonksiyon_adi,liste_adi))
"""

# Soru1
# a=[2,4,5,8] listesindeki elemanların iki katını bularak yeni bir liste yapın

#1. yol
y=[]
a=[2,4,5,8]
def ika(x):
    return 2*x
for k in a:
    y.append(ika(k))
print(y)

#2. yol
y=[]
a=[2,4,5,8]
def ika(x):
    return 2*x
y=list(map(ika,a))
print(y)

#Soru2
# elemanların 3*(liste ismi)+5 değerini bul
# 1. yol
y=[]
a=[2,4,5,8]
list(a)
for k in a:
    y.append(3*k+5)
print(y)

# 2. yol
y=[]
a=[2,4,5,8]
def tg(x):
    return 3*x+5
y=list(map(tg,a))
print(y)

#Online derste çözülen örnek 1
# p=[5,9,2,7] listesinin 3x+7 değerlerini döndüren fonksiyonu map ile bulunuz
y=[]
p=[5,9,2,7]
def tc(x):
    return 3*x+7
y=list(map(tc,p))
print(y)

#Soru 3
#elemanların karesini alın
# 1. yol
y= []
a=[2,4,5,8]
list(a)
for k in a:
    y.append(k*k)
print(y)

#2. yol
y=[]
a=[2,4,5,8]
def ka(x):
    return x*x
y=list(map(ka,a))
print(y)

#Soru 4
# m=[2,3,8,5,4,6] listesindeki elemanları tek ve çifte göre ayır
y=[]
m=[2,3,8,5,4,6]
def cif(x):
    if x%2==0:
        return "çift"
    else:
        return "tek"
y=list(map(cif,m))

print(y)

#Soru 5
#canta=["kalem","silgi","defter"]
#["kalem","cetvel","makas","silgi"] elemanları canta listesinde varsa var yoksa yok yazdırın
y=[]
m=["kalem","cetvel","makas","silgi"]
def bul(z):
    canta=["kalem","silgi","defter"]
    if z in canta:
        return "var"
    else:
        return "yok"

y=list(map(bul,m))
print(y)

#FİLTRELEME METODU
#Bir mantıksal fonksiyona liste elemanlarını gönderdiğimizde mantıksal fonksiyon sonucu doğru olarak dönen değerleri yeni bir listeye atar

#Soru6
# e=[3,5,8,4,7] bu listede tek olan sayıları gösteriniz
e=[3,5,8,4,7]
def tg(x):
   return x %2!=0

y=list(filter(tg,e))
print(y)

#Soru 7
# e=[3,5,8,4,7] bu listede 5'ten büyük olan sayıları yazdırın
e=[3,5,8,4,7]
def buy(x):
    return x>5

y=list(filter(buy,e))
print(y)

#Soru 8
#canta=["kalem","silgi","defter"]
#["kalem","cetvel","makas","silgi"] elemanları canta listesinde olmayanları yazdırın 

y=[]
m=["kalem","cetvel","makas","silgi"]
def var(x):
    canta=["kalem","silgi","defter"]
    return x not in canta 

y=list(filter(var,m))
print(y)

#Online derste çözülen örnek 2
#l=[5,9,12,6,4] listesindeki elemanların çift olanlarını yazdırın

y=[]
l=[5,9,12,6,4,82,96,7425]
def cift(x):
    return x%2==0

y=list(filter(cift,l))
print(y)