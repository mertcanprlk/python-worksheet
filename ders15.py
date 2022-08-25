#KABARCIK SIRALAMA#
#Küçükten büyüğe sıralama yapıyoruz ama sıra sıra yapıyoruz

"""
1. adım 3 5 2 1 4 
2. adım 3 2 5 1 4
3. adım 3 2 1 5 4
4. adım 3 2 1 4 5
5. adım 2 3 1 4 5
6. adım 2 1 3 4 5
7. adım 1 2 3 4 5
"""

#önce 3 ile 5e bakıyoruz 3<5'ten küçük olduğu için bir şey değişmeyecek (1. adım) sonra 5 ve 2'ye bakıyoruz ondan sonra 2<5 olduğu için 2 ile 5'in yeri değişir (2. adım).
#Bu şekilde tek tek bakıyoruz daha sonra mevcut durum 4. durumda son bulduğunda tekrardan sıralamaya bakılır yani sıralı dizide küçük olanların başa gelmesi için her adımı yapacağız

#ARAYA YERLEŞTİRME#
#Kabarcık sıralama'nın daha hızlısı 

"""
1. adım 3 5 2 1 4 
2. adım 2 3 5 1 4
3. adım 1 2 3 5 4
4. adım 1 2 3 4 5
"""

#Bütün sıralamalarda 1. adıma bağlı kalarak sıralama yapıyoruz en küçüğünü bulduğumuz an başa yazıyoruz onu yani 3 5 2 1 sıralı dizisinde 3'ü hafızamıza aldıktan sonra en küçük karşılaştığımız rakam 2 olduğu için onu baş yazdık 1'e bakmadık 
# kabarcık sıralamadan farklı her adım, her adım içindeki sıralı dizisinde sıralanır 

#SEÇMELİ ALGORİTMA#

"""
1. adım 3 5 2 1 4 
2. adım 1 5 2 3 4
3. adım 1 2 5 3 4
4. adım 1 2 3 5 4
5. adım 1 2 3 4 5
"""

#Burada baştaki rakam olan 3'ü seçiyoruz önce 5'e baktık sonra 2'ye sonra 1'e sonra 4'e baktık burda bu adımdaki en küçükle ilk aldığımız sayının yerleri değişir. Böyle böyle sıralarız

#Örnek 1 
#Kabarcık örnek

"""
3 8 2 9 6 1
3 2 8 9 6 1
3 2 8 6 9 1 
3 2 8 6 1 9
2 3 8 6 1 9
2 3 6 8 1 9
2 3 6 1 8 9
2 3 1 6 8 9
2 1 3 6 8 9
1 2 3 6 8 9
"""

#Örnek 2
#Araya Yerleştirme

"""
3 8 2 9 6 1
2 3 8 9 6 1
2 3 6 8 9 1
1 2 3 6 8 9
"""

#Örnek 3
#Seçmeli algoritma

"""
3 8 2 9 6 1
1 8 2 9 6 3
1 2 8 9 6 3
1 2 3 8 9 6
1 2 3 6 8 9
"""

