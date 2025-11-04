# python izohli lugatlarini yaratamiz va ularni alifbo tartibida konsolga chiqaramiz


lugat = {
     "for" : "biror qiymatni qayta bajarilish tsikli",
     "string" : "matn korinishidahi qiymat",
     "float" : "son ko'rinishidagi qiymat",
     "in" : "biror narsani ichidan qiymat olish",
     "integer" : "butun son",
     "else" : "ifdan song keladi faqat bir marta ishlatiladi aks holda degani",
     "elif" : "aks holda",
     "bolean" : "biror qiymatni qayta bajarilish tsikli",
     ".title()" : "soz bosh harfini katta qiladi",
 }
 
print("pythondagi qiymatlar: ")
 
for lugat_k , lugat_q in lugat.items():
  
      print(f"{lugat_k.title()} - {lugat_q}")


#  davlatlar va ularning poytaxti haqidagi lugatni yaratamiz va alifbo tartibida chiqaramiz


davlat = {
    "AQSH": "Washington",
    "ITALIYA": "Rim",
    "MALAYZIYA": "Kuala Lumpur",
    "O'ZBEKISTON": "Toshkent",
    "QIRG'IZISTON": "Bishkek",
    "QOZOG'ISTON": "Nursulton",
    "SINGAPUR": "Singapur",
    "TOJIKISTON": "Dushanbe",
    "ROSSIYA": "Moskva"
}

print(" DAVLATLAR :")
for davlat_nomi in sorted(davlat):
    print(f"{davlat_nomi.title()} — {davlat[davlat_nomi].title()}")

print("\n DAVLATLAR POYTAXTLARI :")
for poytaxt in sorted(davlat.values()):
    print(poytaxt.title())




# foydalanuvchidan davlat nomini kiritishini soraymiz agar bor bolsa poytaxtini chiqaramiz agar bolmasa yoq deymiz

davlat_kiriting = input("DAVLAT NOMINI KIRITING: ")


davlatlar = {
    "AQSH": "Washington",
    "ITALIYA": "Rim",
    "MALAYZIYA": "Kuala Lumpur",
    "O'ZBEKISTON": "Toshkent",
    "QIRG'IZISTON": "Bishkek",
    "QOZOG'ISTON": "Nursulton",
    "SINGAPUR": "Singapur",
    "TOJIKISTON": "Dushanbe",
    "ROSSIYA": "Moskva"
}


if davlat_kiriting in davlatlar:
     print(f"{davlat_kiriting} ning poytaxti {davlatlar[davlat_kiriting]}")

else : 
     print(f"{davlat_kiriting} davlatining poytaxti haqida malumot yoq")     



# taomlar lugatini yaratamiz va foydalanuvchidan taom soraymiz agar taom bolsa narxini chiqaramiz bo'lmasa taom yoq deymiz


taomlar = {
     "osh" : "45.000 so'm",
     "somsa" : "15.000 so'm",
     "lag'mon" : "35.000 so'm",
     "kabob" : "32.000 so'm",
     "manti" : "11.500 so'm",
     "norin" : "20.000 so'm",
     "chuchvara" : "24.500 so'm",
     "honim" : "20.000 so'm",
     "sho'rva" : "30.000 so'm",
}

print("3 ta ovqatni buyurtma qiling")
taom_buyurtma_1 = input("Birinchi Buyurtma bermoqchi bo'lgan taom nomini kiriting: ")
taom_buyurtma_2 = input("Ikkinchi Buyurtma bermoqchi bo'lgan taom nomini kiriting: ")
taom_buyurtma_3 = input("Uchinchi Buyurtma bermoqchi bo'lgan taom nomini kiriting: ")

taom_buyurtma = [taom_buyurtma_1 , taom_buyurtma_2, taom_buyurtma_3]

for taom_buyurtma_ok in taom_buyurtma:
   if taom_buyurtma_ok in taomlar:
     print(f"{taom_buyurtma_ok} ning narxi {taomlar[taom_buyurtma_ok]}")
   else:
     print(f"Kechirasiz,  bizda {taom_buyurtma_ok} yoq ")     


