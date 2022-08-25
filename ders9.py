# Soru 1
# Verilen iki sayıdan küçük  olanı döndüren fonksiyonu yazın.

def kucuk_bulma(a,b):
    if a>b:
        print(b) 
    else:
        print(a)

a=5
b=1
kucuk_bulma(a,b)

#Soru 2
#Haftanın gün sayısına göre gün adını döndüren fonksiyonu yazınız
def gunAdi(k):
    if k ==1:
        return "pazartesi"
    elif k==2:
        return "salı"
    elif k==3:
        return "çarşamba"
    elif k==4:
        return "perşembe"
    elif k==5:
        return "cuma"
    elif k==6:
        return "cumartesi"
    elif k==7:
        return "pazar"

k=gunAdi(7)
print(k)

#Soru3
#Verilen metinde kaç tane e karakteri olduğunu döndüren fonksiyonu yazınız.
def e_say(k):
    say = 0
    for x in k:
        if x =='e':
            say = say +1
    return say
k=e_say("kelebekler yedi gün yaşar")
print(k)

#def a(a,b=0,c) bu komut çalıştırılamaz çünkü sonda olan c hariç diğer hiç bir değişken 0 olamaz

#Soru 4
#Verilen üç sayının en küçüğünü bulup döndüren fonksiyonu yazınız
def kucuk_bulma(a,b,c):
    if a<b and a<c:
        print(a)
    elif b<c and b<a:
        print(b)
    else:
        print(c)


kucuk_bulma(5,0,2)
#2. yol 
def  ek2(a,b,c):
    if a>b:
        if b>c:
            print (c)
        else:
            print (b)
    elif a>c:
        print (c)
    else:
        print (a)

ek2(8,6,9)

# Swap(Yer değiştirme) Algoritması: İkideğişken değerinin karşılıklı olarak yer değiştirmesidir.
a=3
b=5

#swap'te ek bir değişken kullanır
k=a
a=b
b=k
print(a,b)


        

