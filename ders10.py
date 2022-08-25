#LİSTELER#
#Köşeli parantezlerin içinde gösterilir. 
#Liste elemanları virgülle ayrılır.
#Elemanlar farklı tiplerde olabilir.
#İlk indeks değeri 0 olarak sıralı bir şekilde indexler atanır

k=[1,"armut",2.9,True]
print(k [1])

k [0] #Bu listenin 1. elemanını gösterir
k [-1] #Bu listenin sonuncu elemanını gösterir

#Sual 1
#2.9 değerindeki elemanı çağırın
print(k[-2])
print(k [2])

#Sual 2
#2. ve 3. elemanı çağırınız 
print(k [2:4]) 

#Sual 3
#Baştan 3. elemana kadar olanı çağırın 
print(k [0:3] ) #Köşeli parantez içine [:] yazılırsa baştaki sayı otomatik 0 olarak belirlenir yani [:]=[0:]  

listem = [1,2,3,4,5,6,7,8]
listem.append(9) #Listenin sonuna eleman ekler
print(listem)

listem.insert(3,"Elma") #Listenin belirtilen yerine yeni eleman ekler
print(listem)

listem.pop() #Listeden elemanı siler eğer parantezin içindekini belirtilirse o elemanı siler.
print(listem)

a=[1,2,3]
b=[8,9,10]
print(a+b) #a ve b listelerini tıpkı string gibi yazdırır
print(2*a) #Listeyi iki kere yazdırır

for k in listem: #Listenin elemanlarını alt alta yazdırır
    print (k)

m=[2,3,[8,9,[5,6]]]
print(m[2][0])
print(m[2][2][0])

ab = [5,6,[7,9]]
#Soru 1
#Listeye 7 rakamını ekleyleyin
ab.append(7)
print(ab)

#Soru2
#Listeye ab'nin 3. indeksine 9 değerli elemanı ekleyin.
ab.insert(3,9)
print(ab)

#Soru3
#ab'nin ilk elemanının değerini 5'ten 8'e değiştirin
ab[0]=8
print(ab)

#Soru 4 
#ab'deki son elemanı sildirin
ab.pop()
print(ab)

#Soru 5
#ab'deki diğer 6 nolu elemanı silin
ab.pop(1)
print(ab)

#Soru 6
# ab'deki ilk 9 değerini çağırın
print(ab[1][1])

m=[9,5,8,6,3]
#Bu listeyi tersine çevirin
m.reverse()
print(m)

#m listesini sıralayın 
m.sort()
print(m)

