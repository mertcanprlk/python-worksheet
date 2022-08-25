#İç içe döngüler
for k in range(1,9):
    for m in range(4,7):
        print(k,m)

#Örn1
# 1 4
# 1 5 
# 1 6 
# 2 4 
# 2 5 
# 2 6 bunlara karşılık gelen kodu yazın
for k in range(1,3):
    for m in range(4,7):
        print(k,m)

#Örn2
# 1
# 1
# 1
# 2
# 2
# 2
# 3
# 3
# 3
# 4
# 4
# 4
# 5
# 5
# 5 tranpozunu yazdırın
for k in range(2):
    for m in range(3):
        print(k)

#Örn3
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
for k in range(3):
    for m in range(1,5):
        print(m)

#Birleştirme Operatörü
#+ operatörü stringlerle kullanıldığında yan yana yazdırılır 

# Örn4
# 555
# 555
# 555
# 555
# '5' ve iç içe döngü kullanarak yukarıyı yazdırın

#***Benim yaptığım yol***
for k in range(555,556):
    for m in range(4):
        print(k)

#***Hocanın yaptığı yol***
for k in range(4):
    f="5"
    for m in range(3):
        f=f+""
    print(f)

#Örn5
#1 2 3 4
#1 2 3 4
#1 2 3 4
#rakam, birleştirme oparatörü ve iç içe döngü kullanarak yapınız
for k in range (3):
    f=""
    for m in range(1,5):
        f=f+ " " + str(m)
    print(f)

#Örn6
# ****
# ****
# ****
# **** 
#kodla yazdırın
for k in range (4):
    f="****"
    for m in range(1,5):
        f=f+" " 
    print(f)

#Örn7
# *
# **
# ***
# ****
#Kodla yazdırın

#**1. yol**
f=""
for m in range(4):
    f=f+ "*"
    print(f)


#**2. yol**
d="*"
print(d)
for m in range(3):
    d=d+ "*"
    print(d)

#Örn8
# *
# ***
# *****
# *******
#Kodla yazdırın
d="*"
print(d)
for m in range(3):
    d=d+ "**"
    print(d)

#Örn9
#a
#r
#a
#b
#a
#Kodla yazdırın
for k in "araba":
    for m in range(2,4):
        print(m,k)
