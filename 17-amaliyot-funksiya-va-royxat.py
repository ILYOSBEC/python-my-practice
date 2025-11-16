# matnlardan royxat qabul qilib har bir so'zni bosh harfini katta qilamiz misol uchun: Ali , Vali


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism] = baho  
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)

print("\nTalabalar baholari:")
for ism, baho in baholar.items():
    print(f"{ism.title()}: {baho}")



# yoquridagi funksiyani yangi ro'yxat qaytaradigan qilib oz'gartiaramiz

def baholash(ismlar):
    baholar = {}
    for ism in ismlar:  # pop() o‘rniga oddiy aylanish
        baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism] = baho  
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = baholash(talabalar)

print("\nTalabalar baholari:")
for ism, baho in baholar.items():
    print(f"{ism}: {baho}")

print("\ntalabalar ikkinchi:")
for ism, baho in baholar.items():
    print(f"{ism.title()}: {baho}")



# bahola funksiyasini .pop() dan foydalanmasdan va royxatda ozgartirish kirtmasdan lugat koronoshida chiqaramiz

def baholaa():
    """O‘quvchilar ro‘yxatini qaytaradi"""
    return ["sarvar", "dilshod", "anvar", "nodir"]

def baho_k():
    """Har bir o‘quvchidan baho kiritish va natijani qaytarish"""
    oquvchilar = {}
    for ism in baholaa():
        baho = input(f"{ism.title()} ning bahosini kiriting: ")
        oquvchilar[ism] = baho
    return oquvchilar


oquvchilar = baho_k()

print("\nO‘quvchilarning baholari:\n")
for ism, baho in oquvchilar.items():
    print(f"{ism.title()} ning bahosi: {baho}")



      
