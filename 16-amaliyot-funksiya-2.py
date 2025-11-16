# 1) foydalanuvchidan ism familiya yoshi relefon raqami kabi narsalarni olib lugat korrinishida chiqaramiz ///


def user_information(ism , familiya , yosh , davlat , viloyat , kasb , t_raqam=None):
    """foydalanuvchidan malumot olamiz"""
    user_lugat = {
        "ismi": ism,
        "familiyasi": familiya,
        "yoshi": yosh,
        "telefon_raqami": t_raqam,
        "davlati": davlat,
        "viloyati": viloyat,
        "kasbi": kasb
    }
    return user_lugat


def user_info():
    """foydalanuvchidan malumot olamiz"""
    malumotlar = []

    ism = input("Ismingizni kiriting: ")
    familiya = input("Familiyangizni kiriting: ")
    yosh = input("Yoshingizni kiriting: ")
    t_raqam = input("Telefon raqamingizni kiriting: ")
    davlat = input("Davlatingizni kiriting: ")
    viloyat = input("Viloyatingizni kiriting: ")
    kasb = input("Kasbingizni kiriting: ")

    malumotlar.append(user_information(ism, familiya, yosh, davlat, viloyat, kasb, t_raqam))
    return malumotlar


malumotlar = user_info()

print('\nFoydalanuvchilarning ma\'lumotlari:')
for malumot in malumotlar:
    print(f"Ism: {malumot['ismi']}")
    print(f"Familiya: {malumot['familiyasi']}")
    print(f"Yosh: {malumot['yoshi']}")
    print(f"Davlat: {malumot['davlati']}")
    print(f"Viloyat: {malumot['viloyati']}")
    print(f"Kasb: {malumot['kasbi']}")
    print(f"Telefon: {malumot['telefon_raqami']}")


# yuqoridagi funksiytani while bilan qilamiz yani yaya qaytarailadigan qilamiz



def user_information(ism , familiya , yosh , davlat , viloyat , kasb , t_raqam=None):
    """foydalanuvchidan malumot olamiz"""
    user_lugat = {
        "ismi": ism,
        "familiyasi": familiya,
        "yoshi": yosh,
        "telefon_raqami": t_raqam,
        "davlati": davlat,
        "viloyati": viloyat,
        "kasbi": kasb
    }
    return user_lugat


def user_info():
    """Bir nechta foydalanuvchidan ma'lumot olish"""
    malumotlar = []

    while True:
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
        yosh = input("Yoshingizni kiriting: ")
        t_raqam = input("Telefon raqamingizni kiriting: ")
        davlat = input("Davlatingizni kiriting: ")
        viloyat = input("Viloyatingizni kiriting: ")
        kasb = input("Kasbingizni kiriting: ")

        malumotlar.append(user_information(ism, familiya, yosh, davlat, viloyat, kasb, t_raqam))

        # Yana ma'lumot qo‘shasizmi?
        javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q): ").lower()
        if javob == "yo'q":
            print(" Ma'lumot kiritish yakunlandi.")
            break
    
    return malumotlar


# 🔹 Funksiyani chaqiramiz
malumotlar = user_info()

print('\nFoydalanuvchilarning malumotlari:')
for malumot in malumotlar:
    print(f"Ismi : {malumot['ismi']}")
    print(f"Familiyasi : {malumot['familiyasi']}")
    print(f"Yoshi : {malumot['yoshi']}")
    print(f"Davlati : {malumot['davlati']}")
    print(f"Viloyati : {malumot['viloyati']}")
    print(f"Kasbi : {malumot['kasbi']}")
    print(f"Telefon raqami : {malumot['telefon_raqami']}")





# 3)  3 ta son qabul qilamiz va ulardan eng kattasini qaytaradi

def son3(sonlar):
    """3 ta son qabul qilib eng kattasini qaytaruvchi funksiya"""
    return max(sonlar)

son_1 = int(input("birinchi sonni kiriting: "))    
son_2 = int(input("ikkinchi sonni kiriting: "))    
son_3 = int(input("uchinchi sonni kiriting: "))   

natija = son3([son_1, son_2, son_3])

print(f"Eng katta son: {natija}")

# 4) foydalanuvchidan aylananinging radiusini qabul qilib uni radiusi peremetri , diametri va yuzini lugat korinshinida chiqaruvci funksiya ///


def aylana(radius):
    """Aylananing radiusi bo‘yicha ma'lumotlarni lug‘atda qaytaradi"""
    pi = 3.14
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * pi * radius,
        "yuza": pi * radius ** 2
    }
    return aylana


kiritish = float(input("Aylananing radiusini kiriting: "))
natija = aylana(kiritish)

print("\nAylananing o'lchamlari:")
print(natija)



# 5) berilgan sonlar orasisgi faqat tub sonlarni qaytaruvchi funksiya //// 


def tubson_funk(min, max):
    """tub sonlarni qaytaruvchi funksiya"""
    sonlar = []
    while min < max:
        if min > 1:
            for sonlar_bc in range(2, min):
                if min % sonlar_bc == 0:
                    break
            else:
                sonlar.append(min)
        min += 1
    return sonlar


print(tubson_funk(10, 100))
print(tubson_funk(50, 500))









