# cars degan ro'yxat yaratamiz 

cars = ["tayotta", "mazda", "huindai", "gm", "kia"]

for car in cars:
    if car == "gm":
        print(car.upper())

    else:
        print(car.title())


# teng emas operatorida bajaramiz 

cars = input("mashina nomini kirting: ")

if cars != "cobalt":
    print("notogri boshqa mashina edi")
else:  
    print("to'gri cobalt")


#foydalanuvchi login ismini so'raymiz

foydalanuvchi_ismi = input("ismingizni kiriting: ")
if foydalanuvchi_ismi != "admin" :
    print("xush kelibsiz ", foydalanuvchi_ismi)
else: 
    print("xush kelibsiz, admin foydalanuvchilar ro'yxatini ko'rasizmi")


# foydalanuvchidan ikta son kiritishii soraymiz gar sonlar tesng bolsa sonlar teng degsn yozuv ni consolga chiqgaramiz 


son1 = input("birinchi sonni kiriting: ")
son2 = input("ikkinchi sonni kiriting: ")

if son1 != son2 :
    print("yozgan sonlaringiz teng emas")
else : 
    print("siz yozgan sonlaringiz teng ekan")    



# foydaloanuvchidan istalgan sonni kiritishini soraymiz va agar son manfiy bolsa konsolga
#  manfiy son degan yozuv chiqadi agar son musbat bolsa musbat degan yozuv chiqadi     

son = int(input("istalgan sonni kirting: "))

if son < 0 : 
    print('siz kiritgan son manfiy')
else :
    print("siz kiritgan son musbat")    



# foydalanuvchidan son kiritishini so'raymiz va son ni manfiy yoki musbatligiga qarab javob beramiz


istalgan_son = int(input("istalgan son kiritng: "))

if istalgan_son < 0 :
    print("musbat son kiritng ")
else  :
    print("siz kiritgan sonning ildizi: ", son**0.5)




