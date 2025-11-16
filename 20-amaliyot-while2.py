# 1) foydalanuvchidan buyurtma qabul  qiluvchi dastur yozamiz




buyurtmalar = []


while True :
     buyurtma_k = input("qanday mahsulot buyurtma bermoqchisiz: ")
     buyurtmalar.append(buyurtma_k)
     yana = input("yana mahsulot buyurtma qilasizmi: (ha/yoq) ")
     if yana == "yoq":
          break
     else:
          continue
     
print("\nsiz buyurtma bergam mahsulotlar:\n")
for buyurtma in buyurtmalar :
  print(f"mahhsulot: {buyurtma}")




# 2) e-bozor yaratamiz va foydalanuvchidan unga mahsulot kiritishini soraymiz yani nomi va narxini


mahsulotlar = {
    "anor" : 12000,
    "olma" : 5000,
    "karam" : 8000,
    "tarvuz" : 21000,
}


while True:
    mahsulot_k = input("e-bozorga mahsulot qo'shing: ")
    mahsulot_narh = input(f"{mahsulot_k} ni narhini kiriitng: ")
    mahsulotlar[mahsulot_k] = mahsulot_narh
    yana = input("yana mahsulot qo'shasizmi: (ha/yoq) ")
    if yana == "yoq":
          break
    else:
          continue
        
    

print("\n\nE-BOZOR dagi mahsulotlar:\n")
for mahsulot_k, mahsulot_narh in mahsulotlar.items():    
  print(f"mahsulot: {mahsulot_k} , va uning narhi {mahsulot_narh} so'm")



# 3)   yuqoridagi ikala dasturni birlashtirmiz yani foydalanuvchi buyurtma beradi agar buyurma bergan mashsulotlar bozorda bolsa narhini 
# # chiqaradi bolmasa bu mahsulot yoq deydi

e_bozor_mahsulotlar = {
    "olma": 12300,
    "anor": 20300,
    "nok": 11000,
    "tarvuz": 15600,
    "banan": 9900,
    "bodiring": 6300,
    "shaftoli": 12300,
    "telefon": 1233300,
    "televizer": 5234000,
    "velasiped": 554000,
    "noutbuk": 657400,
}

buyurtmalar = [] 

while True:
    print("\nAssalomu alaykum, E-BOZORGA xush kelibsiz!\n")
    buyurtma = input("Nima sotib olmoqchisiz kiriting: ")

    buyurtmalar.append(buyurtma)

    yana = input("Yana biror narsa olasizmi? (ha/yoq): ")
    if yana == "yoq":
        break

print("\nSiz sotib olgan mahsulotlar:\n")

for mahsulot in buyurtmalar:
    if mahsulot in e_bozor_mahsulotlar:
        print(f"{mahsulot} - {e_bozor_mahsulotlar[mahsulot]} so'm")
    else:
        print(f"{mahsulot} - do'konimizda yo'q!")







