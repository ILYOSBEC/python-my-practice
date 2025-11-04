#  foydalanuvchidan juft son kiritishi ni soraymiz agar juft son kiritsa rahmat agar toq so kiritsa bu son juf emas degan xabarni chiqaramiz 

juft_son = int((input)("istalgan juf son kiriting: "))

if juft_son % 2 == 0 :
    print("Rahmat")
else :
    print("bu son juft son emas")    


# foydalanuvchidan yoshni soraymiz va yoshiga qarab muzeyga kirish narxini aytamiz

muzeyga_kirish = int(input("yoshingizni kiriting: "))    

if muzeyga_kirish <=4 or muzeyga_kirish >=60 :
    narx = 0
elif  muzeyga_kirish <=18 :
    narx = 10000
elif muzeyga_kirish >18 :
    narx : 20000   

print(f"muzeyga kikish uchun {narx} so'm to'lashingiz kerak ")      



# foydalanuvchidan 2ta son kiritishni soraymiz va ularni teng katta yoki kichigligi haqida malumot chiqaramiz

son1 = int(input("birinchi sonni kiritng: "))

son2 = int(input("ikkinchi sonni kirting: "))

if son1 < son2 :
    print(son1 , " < " , son2)
    
elif son1 > son2 :
    print(son1 , " > " , son2)
elif son1 == son2:
    print(son1 , " = " ,son2)    



#  mahsulotlar va savat degan royxatlar yaratamiz va foydalanuvchidan 5 ta mahsulot kiritishini soraymiz

mahsulotlar = ["anor", "shaftoli", "un", "olma", "go'sht", "non", "piyoz"  , "guruch" ,"pista" , "yon'goq"]

savat = []

savat1 = input("savatga 1-mahsulotni soling: ")
savat2 = input("savatga 2-mahsulotni soling: ")
savat3 = input("savatga 3-mahsulotni soling: ")
savat4 = input("savatga 4-mahsulotni soling: ")
savat5 = input("savatga 5-mahsulotni soling: ")


for savat in savat1 , savat2 , savat3 , savat4 , savat5  :
 if savat in mahsulotlar :
    print(f"bizda {savat} bor")
if  savat not in mahsulotlar :  
    print(f"uzr, bizda {savat} yo'q ekan")



#  yuqoridagi dastruni biroz o'zgartriamiz yani foydalanuvchidan 5 ta ta mahsulot soraymiz va bor_mahhsolot va mavjud_emas degan ro'yxatlar ham yaratamiz


dokon = ["non", "un", "telefon", "televizer", "velosiped", "go'sht", "olma"]

bor_mahsulotlar = []
mavjud_emas = []

mahsulot_1 = input("1-mahsulotni kiriting: ")
mahsulot_2 = input("2-mahsulotni kiriting: ")
mahsulot_3 = input("3-mahsulotni kiriting: ")
mahsulot_4 = input("4-mahsulotni kiriting: ")
mahsulot_5 = input("5-mahsulotni kiriting: ")

soralganlar = [mahsulot_1, mahsulot_2, mahsulot_3, mahsulot_4, mahsulot_5]

for mahsulot in soralganlar:
    if mahsulot in dokon:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if bor_mahsulotlar:
    print(f"Do‘konimizda bor mahsulotlar: {bor_mahsulotlar}")
if mavjud_emas:
    print(f" do'konimizda bu mahsulotlar yo‘q: {mavjud_emas}")



# foydalanuvchilar degan royxat  yaratamiz va login tizimini qo'shamiz

foydalanuvchilar = ["ilyos", "login1" , "login2" , "parol" , "maxfiy" , "picaviy"]

yangi_foydalanuvchi = input("loginingizni kirting: ")

if yangi_foydalanuvchi in foydalanuvchilar :
    print("bu login allaqachon qolingan iltimos bsohqa login kiritng")
else:
    print("xush kelibsiz, yangi foydalanuvchi !!!")    



# foydalanuvchidan butun son kirtishini soraymiz va uni 2 dan 10 gacha bolgan sonlardan qaysiga bolishinishini konolgan chiqaramiz


butun_son = int(input("istalgan butun son kiring: "))

if butun_son % 2 == 0 :
    print(f"{butun_son} 2 ga qoldiqsiz bo'linadi")
if butun_son // 3 :
    print(f"{butun_son} 3 ga qoldiqsiz bo'linadi")   
if butun_son // 4 :
    print(f"{butun_son} 4 ga qoldiqsiz bo'linadi")
if butun_son // 5 :
    print(f"{butun_son} 5 ga qoldiqsiz bo'linadi")
if butun_son // 6 :
    print(f"{butun_son} 6 ga qoldiqsiz bo'linadi")
if butun_son // 7 :
    print(f"{butun_son} 7 ga qoldiqsiz bo'linadi")
if butun_son // 8 :
    print(f"{butun_son} 8 ga qoldiqsiz bo'linadi")
if butun_son // 9 :
    print(f"{butun_son} 9 ga qoldiqsiz bo'linadi")
if butun_son // 10 :
    print(f"{butun_son} 10 ga qoldiqsiz bo'linadi")    