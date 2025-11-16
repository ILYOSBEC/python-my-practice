# islatgancha sonlarni qabul qilib ularni ko'paytmasini qaytaruvchi funksiya yozamiz


def kopaytirish(min_son, max_son):
    natija = 1
    for son in range(min_son, max_son + 1):
        natija *= son
    return natija


print(kopaytirish(1, 5)) 
print(kopaytirish(5, 10))  
print(kopaytirish(1, 10))  
print(kopaytirish(1, 20))  










# talabalr haqidagi malumot ni lugat korinishda qaytaruvchi funksiya yozamiz va  ism familiyasi va boshqalar va bazilarini ixtiyoriy qilamiz

def talabalar_info(ism, familiya, yosh, yonalish, ota_ism=None):
    """Talaba haqidagi ma’lumotlarni lug‘at shaklida qaytaruvchi funksiya"""
    t_info = {
        "ismi": ism,
        "familiyasi": familiya,
        "yoshi": yosh,
        "yonalishi": yonalish,
        "otasining ismi": ota_ism if ota_ism is not None else "ma'lumot yo'q"
    }
    return t_info


talaba_01 = ["Ilyosbek", "Ro'ziyev", 15, "Dasturlash"]
talaba_02= ["jasur", "azamatov", 25, "tibbiyot" , "anvar"]
talaba_03 = ["sunnat", "qudratov", 20, "moliya" , "dilshod"]
talaba_04 = ["ali", "valiyev", 19, "kiber xavfsizlik"]

talabalar_data_all = [talaba_01, talaba_02, talaba_03, talaba_04]

for talaba in talabalar_data_all:
    talabalar_data = talabalar_info(*talaba)
    print(talabalar_data)
    



   




