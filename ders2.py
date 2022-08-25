#Karşılaştırma Operatörleri#

print(3>5)
print('araba' < 'kum') 
#>, <, <=,>=,== (karşılaştırma için), !=
##bool çevirilerinde bool(0) haricinde hepsi true olarak gösterilir

#Mantıksal Operatörler#

# True and True -> True
#  T and F -> False
#  F and T -> False
#  F and F -> F

#  T or T -> T
#  F or T -> T
#  T or F -> T
#  F or F -> F

# not F -> T
# not T -> F

print(3<5 or 5>1)
print(5>7 and 9<1 or 6<4) #parantezlerle işlem önceliği de yaptırabilirsin
print(not 0<5)

#Soru 1# 
#1den büyük ve 7 ve 7den küçük sayıların doğru değerlerinin false ve true olduğu kodu yazın
k=8
print(k>1 and k<=7)
a=5
print(not(k>7 or k<=1))

#Soru 2#
#-3den küçük ve 2den büyük sayıların doğru değerlerinin false ve true olduğu kodu yazın
b=31
print(b<=-3 or b>2)
print(not(b>-3 and b<=2))

#Soru 3#
#-3 ve -1 ayrıca 1 ve 4 arasında değerleri false yazan kod yazınız
c=0
print(c<-3 or (c>-1 and c<=1) or c>4)
print(not((c>=-3 and c<=-1)or(c>1 and c<=4)))

#Soru 4#
#(-5,3] ile 2de büyük sayıların false döndüğü yerde kkullanıldığında girilern sayının ne olduğunu gösterin

f=input("lütfen sayı giriniz")
f=int(f)
print(f<-5 or (f>=-3 and f<=2))