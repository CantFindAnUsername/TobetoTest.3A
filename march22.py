#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

"""  fibonacci = [1, 1]

while len(fibonacci) < 20:  # En az 20 elemanlı olana kadar devam et
    next_number = fibonacci[-1] + fibonacci[-2]  # Son iki elemanın toplamı
    fibonacci.append(next_number)

print(fibonacci) """

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

""" def mukemmel_mi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

sayi = int(input("Bir sayı girin: "))

if mukemmel_mi(sayi):
    print(sayi, "bir mükemmel sayıdır.")
else:
    print(sayi, "bir mükemmel sayı değildir.") """

#3- Kullanıcının giridiği iki sayının EBOB ve EKOK'unu bulan programı yazınız.

""" def ebob_ekok_hesapla(birinciSayi, ikinciSayi):
    # EBOB hesaplama
    if birinciSayi > ikinciSayi:
        kucuksayi = ikinciSayi
    else:
        kucuksayi = birinciSayi
    for i in range(1, kucuksayi + 1):
        if (birinciSayi % i == 0) and (ikinciSayi % i == 0):
            ebob = i
            
    # EKOK hesaplama
    ekok = (birinciSayi * ikinciSayi) // ebob
    return ebob, ekok
 
birinciSayi = int(input("Birinci Sayıyı Giriniz: "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz: "))
 
ebob, ekok = ebob_ekok_hesapla(birinciSayi, ikinciSayi)
print("EBOB:", ebob)
print("EKOK:", ekok) """

#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

""" sayi = int(input("Bir sayı girin: "))
asalmi = True

if sayi == 1 :
    asalmi = False
for i in range(2,sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi :
    message = "Girdiğiniz sayı asaldır."
else :
    message = "Girdiğiniz sayı asal değildir"

print(message) """

#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

""" number = int(input("Lütfen bir sayı giriniz: "))
primeFactor = 2
print(number, "sayısının asal çarpanları:")
for i in range(1, number):
    if (number % primeFactor ==0):
        print(primeFactor)
        number /= primeFactor
    else:
        primeFactor+=1 """








