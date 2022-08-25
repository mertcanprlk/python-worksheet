#Range Kullanımı
x =1
for x in range(1,10):
    print(x)

x = list(range(6,10))
print(x)

x = list(range(6,100,5))
print(x)

#Örn1
#3'ten 9'a kadar olan sayıları 5 ve 7 dışında gösterin.
numbers = [x for x in range(3,9) if x!=5 and x!=7]
print(numbers)

#Örn2
#7'den 14'e kadar olan sayıların toplamını bulup ekranda gösteriniz
toplam=0
for x in range(7,14):
    toplam = toplam +x
print(toplam)

#Örn3
#6'dan 18'e kadar olan çift sayıların toplamını bulunuz
toplam=0
for x in range(6,18):
    if x % 2 == 0:
        toplam = toplam +x
print(toplam)

#Örn4
#12'den 30'a kadar 3'er artarak giden sayıların çarpımı
carp=1
for x in range(12,30):
    if x % 3 == 0:
        carp = carp*x
print(carp)

#Örn5
#1247'den 1298'e kadar olan sayılarda 17 ile bölünenleri ekranda gösteriniz
for x in range(1247,1298):
    if x % 17 == 0:
        print(x)

for x in 'Slm':
    print(x)

#örn6
#Bugün hava güzel metninde karakter sayısı kaçtır
say = 0
for x in 'Bugün hava güzel':
    say = say +1
print(say)

#Örn7
#"Adanada hava çok sıcak" metnindeki" 'a' karakterlerini saydırınız
k = 'Adanada hava çok sıcak'
k=k.lower()
say = 0
for x in k:
    if x =='a':
        say = say +1
print(say)

#örn8
#'Bubam bana bursa'dan bebe aldı' 'b' karakterlerini saydırın.
k = 'Bubam bana bursadan bebe aldı'
k=k.lower()
say = 0
for x in k:
    if x =='b':
        say = say +1
print(say)