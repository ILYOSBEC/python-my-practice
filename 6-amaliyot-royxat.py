# davlatlar royxatini tuzish. royxat uzunligni konsolga chiqaramiz

davlatlar = ['uzbekiston', 'amerika', 'britaniya', 'rossiya', 'kanada', 'ispaniya', 'turkiya']

davlatlar.sort()
print(davlatlar)

print("uzunligi: ", len(davlatlar))

#royxatni sorted yordamida teskari qilamiz

davlatlar2 = ['uzbekiston', 'amerika', 'britaniya', 'rossiya', 'kanada', 'ispaniya', 'turkiya']
print(sorted(davlatlar2, reverse=True))

# 120 dan 1200 gacha bolgan juft sonlar royxati. sonlarni yogorndisni chiqarish

sonlar = list(range(120,1201,2))

print(sonlar)

yigindisi = sum(sonlar)

print("yig'indisi: ", yigindisi )

# eng katta sondan eng kichigini ayirish va royxatdagi elementlar sonini xissoblaymiz

eng_kichik = min(sonlar)

eng_katta = max(sonlar)

print(eng_katta - eng_kichik)

print("elementlar soni: ", len(sonlar))

# royxatni boshidan oxiridan va o'rtasinbdan 20 ta qiymatni konsolga chiqaramiz


boshi = sonlar[0:20]

ortasi = sonlar[len(sonlar)//2 - 10 : len(sonlar)//2 + 10]

oxiri = sonlar[-20:]

print("boshi: ", boshi, " o'rtasi: ", ortasi, " oxiri: ", oxiri)

# taomlar degan royxat yaratmiz va ichiga 5 ta taom nomini yozamiz

taomlar = ["manti", "somsa", "polov", "sho'rva", "shashlik"]

nonushta = taomlar

nonushta.append("lavash")
nonushta.append("pitsa")

print("taomlar ro'yxti: ", taomlar)

print("nonushta uchun taomlar: ", nonushta)









