#Birleştirmeli Sıralama#
"""
Adım 1. 3 8 2 4 7 1 5 6 
Adım 2. 3 8 2 4   7 1 5 6 #Diziyi ikiye ayırdık
Adım 3. 3 8   2 4    7 1   5 6  #İkiye bölümnen diziyi yine ikiye böldük 
Adım 4. 3 8   2 4    1 7   5 6  #İkiye bölünen dizinin ikiye tekrar bölünen tarafında sayılar karşılaştırmalı olarak yeniden düzenlenir küçükler sola büyükler sağa geçer
Adım 5. 2 3 4 8      1 5 6 7 #Bu sefer 1 
Adım 6. 1 2 3 4 5 6 7 8 
"""

"""
12 8 9 7 2 4
12 8 9   7 2 4 #2 parçaya ayırdık
12   8   9         7   2   4 #Bütün hepsini ayırdık
8 12    9          2 7     4 #Sıralı dizileri birleştirmeye başladık
8 9 12      2 4 7 #2 parçaya ayrılanları düzenledik 
2 4 7 8 9 12 
"""

#Hızlı sıralama algoritması#
"""
1. adım 12 8 9 7 2 4 #en sağdaki rakamı seçtik (4'ü yani)
2. adım 2 8 9 7 12 4 #4'e soldan baktık solda gördüğümüz en büyük ilk sayıyı (12yi) seçti daha sonra sağdan en küçük sayıyı buldu (2'yi) sonra bu sayıların yerlerini birbiriyle değiştirdi
3. adım 2 4 9 7 12 8 #Sağdan tekradan baktık gördüğümüz en büyük ilk sayıyı (8'i) seçtik daha sonra sağdan baktık en küçük sayı için 4ten küçük hiç bir sayı bulamadık o zaman sağdan bulduğumuz en büyük sayı (8) ve 4 yer değiştirir
4. adım 2 4 7 9 12 8 #8'e soldan baktık solda gördüğümüz en büyük ilk sayıyı (9u) seçtik daha sonra sağdan en küçük sayıyı buldu (7'yi) sonra bu sayıların yerlerini birbiriyle değiştirdi
5. adım 2 4 7 8 12 9 #8e soldan baktık gördüğümüz en büyük ilk sayıyı (9'u) seçtik daha sonra sağdan baktık en küçük sayı için 8ten küçük hiç bir sayı bulamadık o zaman sağdan bulduğumuz en büyük sayı (9) ve 8 yer değiştirir
6. adım 2 4 7 8 9 12 #9'a soldan baktık gördüğümüz en büyük ilk sayıyı (12'u) seçtik daha sonra sağdan baktık en küçük sayı için 9dan küçük hiç bir sayı bulamadık o zaman sağdan bulduğumuz en büyük sayı (12) ve 9 yer değiştirir
"""

#KÜMELİ SIRALAMA SINAVDA SORULMAYACAK#

#Binary sıralama


