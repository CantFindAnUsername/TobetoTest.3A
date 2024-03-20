# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

#boy = float(input("lütfen boyunuzu (metre cinsinden) giriniz:"))
#agirlik = float(input("lütfen kilonuzu giriniz:"))
#vki = agirlik/(boy * boy)
#print(vki)

# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

#maas = float(input("Lütfen maaşınızı giriniz:"))
#zamOrani = float(input("Lütfen zam oranını giriniz:"))

#total = maas + (maas * zamOrani)

#print(total)

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
'''
num1 = int(input("İlk sayıyı giriniz: "))
num2 = int(input("İkinci sayıyı giriniz: "))
num3 = int(input("Üçüncü sayıyı giriniz: "))
bigNum = 0

if num1 > num2:
    bigNum = num1
else:
    bigNum = num2
if num3 > bigNum:
    bigNum = num3
else:
    bigNum = bigNum
print(bigNum)         
'''
# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
'''
r = float(input("r yarı çapı giriniz: "))

alan = 3.14 * ( r ** 2)

cevre = 2 * 3.14 * r

print(f".alan: {alan}")
print(f".cevre: {cevre}")
'''

# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

#number = int(input("Lütfen palindrom bir sayı giriniz: "))

#numberStr = str(number)

#print(numberStr)


def palindrom_mu(sayi):
    # Sayıyı string olarak dönüştürelim
    sayi_str = str(sayi)
    # Sayının tersini alalım
    ters_sayi_str = sayi_str[::-1]
    # Ters çevrilmiş sayı, aslında giriş sayısıyla eşit mi kontrol edelim
    return sayi_str == ters_sayi_str

# Kullanıcıdan bir sayı girişi alalım
sayi = int(input("Bir sayı girin: "))

# Palindrom olup olmadığını kontrol edelim
if palindrom_mu(sayi):
    print("Girdiğiniz sayı bir palindromdur.")
else:
    print("Girdiğiniz sayı bir palindrom değildir.")
