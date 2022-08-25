a = list(range(3,45,5))
print(a)

# 18 değerine sahip elemanı indeksle çağırın
print(a [3])

#13 değerinden 33 değerine kadar olan elemanları indeksle çağırın
print(a[2:6])

#4. indeksli eleman olarak 5 ekle 
a.insert(4,5) #4. indekse 5 adlı elemanı ekler
print(a)

# Soru1
# a liste değerlerinin iki katını yeni listeye yazdırın
yeni_liste=[]
for k in a:
    yeni_liste.append(k*2)
print(yeni_liste)

#Soru 2
# a listesinde 2'ye ve 3'e bölünenleri
yeni_liste_b=[]
for k in a:
    if k % 2 ==0 and k % 3==0:
        yeni_liste_b.append(k)
print(yeni_liste_b)

#Soru 3
#a listesinde tek ve çift sayıları ayrı ayrı listelerde yazdırın
yeni_liste_c=[]
yeni_liste_d=[]
for k in a:
    if k % 2 ==0:
        yeni_liste_c.append(k)
    elif k % 2==1:
        yeni_liste_d.append(k)
    #elif k %2==1: yapacağına else diyip: geçebilirsin
print(yeni_liste_c)
print(yeni_liste_d)

#Liste içinde bir elemanın olup olmadığının sorgulanması hakkında bazı mülahazalar şamildir
print(9 in a) 

# Soru 4
# a listesinde kullanıcın girdiği değer varsa "var" yoksa "yok" yazdırın
z=int(input("Sayi gir uşağum: "))
if z in a:
    print("var")
else:
    print("yok")

#Soru 5
#Haftanın gün adını verilen gün sayısına göre yazdırın
def hff(e):
    hafta_gun = ["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"] #Fonksiyonun içinde çalıştırılırsa hafızada tutulur ama gösterilmez dışında gösterilirse kalıcı olur
    print (hafta_gun[e-1])
hff(3)