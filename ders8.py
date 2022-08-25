#Fonksiyon komutu
#parametresiz fonksiyorn tanımlama
"""
def foknadi(parametre1,paarmetre2):
    kodlar   
    kodlar 
    return geriye_dönecek_değer
"""

# örn1
#merhaba yazan fonksiyon tanmlayın
def a():
    print('merhaba')

a()

#Parametre ile fonksiyon tanımlama
#Örn2
#verilen iki sayıyı toplayan foksiyonu yazın

def topla(a,c):
    print(a+c)

topla(2,2)

#parametre sıralaması önemlidir
#Örn3
#verilen iki sayının farkını alan fonksiyonu yazınız
def cıkar(a,b):
    print(a-b)

cıkar(2,9)
cıkar(9,2)

#Örn 4
#3 sayının çarpımını alan fonksiyonu yazın
def carp(a,b,c):
    k= a*b*c
    print(k)

carp(2,9,8)
carp(9,2,5)

#Fonksiyonlarda parametre sırası değişir
def cıkar(a,b):
    print(a-b)

cıkar(a=9,b=6)

#Örn5
# dik kenarın ve hipotenüsün verilerek, diğer dik kenarın bulunduğu fonksiyonu yazın
def diger(d,e):
    print((e*e-d*d)**0.5)
    
diger(d=5,e=13)

#Varsayılan değerlerle fonksiyon oluşturma
"""
def va(varsayimsiz_parametre1,varsayimsiz_parametre2,vasayimli_parametre=3)
"""

#Örn6
#Verilen dört sayıya kadar toplamın bulan fonksiyonu bulun
def topla(a,b,c=0,d=5): #c ve d varsayılan fonksiyonlardır eğer topla kısmında gösterilmezse başta belirtilen varsayılan değerde kullanılır
    print(a+b+c+d)

topla(1,2,3,4)
topla(1,2,3)
topla(1,2)
"""
topla(1) #Bu komut çalışmaz en az varsayılansız kadar parametre gönderilmelidir
"""

# Örn7
def carp(a=5,b=4):
    print(a*b)

carp()

#Örn8
#Kullanıcı adı ve doğum yılı gönderilen bir fonksiyonda 
#   sayın ....., ..... yaşındasınız yazdırınız.
def dogumgunu(a,b):
    a= str(a)
    b= int(b)
    c=2022 -b
    print(f"sayın {a} , {c} yaşındasınız")

dogumgunu("mertcan", 2002)

##2. yol 
def yaz(k,m):
    print("sayın" + k + ", " + str(2022-m) + "yaşındasınız")

yaz("mert",2002)

for x in range(2,5):
    print(x)