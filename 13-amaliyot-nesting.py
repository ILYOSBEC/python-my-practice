# dostlarimning sevimli 3 ta kinolarini so'rayman va konsolga chiqaraman

print("Salom Sarvar ! Sevimli 3 ta filmingiz nomini kiriting:")

film_1 = input("Birinchi sevimli filmingizni kiriting: ")
film_2 = input("Ikkinchi sevimli filmingizni kiriting: ")
film_3 = input("Uchinchi sevimli filmingizni kiriting: ")

print("Salom ilyosbek ! Sevimli 3 ta filmingiz nomini kiriting:")

film_4 = input("Birinchi sevimli filmingizni kiriting: ")
film_5 = input("Ikkinchi sevimli filmingizni kiriting: ")
film_6 = input("Uchinchi sevimli filmingizni kiriting: ")

print("Salom Dilshod ! Sevimli 3 ta filmingiz nomini kiriting:")

film_7 = input("Birinchi sevimli filmingizni kiriting: ")
film_8 = input("Ikkinchi sevimli filmingizni kiriting: ")
film_9 = input("Uchinchi sevimli filmingizni kiriting: ")

foydalanuvchilar = {
    "Sarvar": {
        "sevimli_film_1": film_1,
        "sevimli_film_2": film_2,
        "sevimli_film_3": film_3
    },
    "ilyosbek" : {
        "sevimli_film_1": film_4,
        "sevimli_film_2": film_5,
        "sevimli_film_3": film_6 
    },
    "Dilshod" : {
        "sevimli_film_1": film_7,
        "sevimli_film_2": film_8,
        "sevimli_film_3": film_9 
    }
    
    
}

for ism, info in foydalanuvchilar.items():
    print(f"\n{ism.title()}ning sevimli filmlari:")
    print(f"{info['sevimli_film_1']}")
    print(f"{info['sevimli_film_2']}")
    print(f"{info['sevimli_film_3']}")


#  davlatlar degan lugat yaratamiz vca unda davlatlarning malumotlarini joylashtiramiz


davlatlar = {
      "o'zbekiston" : {
          "potaxti" : 'Toshkent',
          "Hududi" : '448 978 km²',
          "Aholisi" : '36,5 million kishi',
          "Pul birligi" : 'So‘m (UZS)',
      },

    "rossiya" : {
          "potaxti" : 'Moskva',
          "Hududi" : '17 098 246 km²',
          "Aholisi" : '145 million kishi',
          "Pul birligi" : 'Rubl (RUB))',
      },

    "amerika" : {
          "potaxti" : 'Vashington (Washington, D.C.)',
          "Hududi" : '9 833 517 km²',
          "Aholisi" : '340 million kishi',
          "Pul birligi" : 'AQSh dollari (USD)',
      },

    "turkiya" : {
          "potaxti" : 'Anqara (Ankara)',
          "Hududi" : '783 562 km',
          "Aholisi" : '86 million kishi',
          "Pul birligi" : 'Turk lirasi (TRY)',
      },
}


for davlat , davlat_info in davlatlar.items():
    print("Dunyo davlatlari haqida ma'lumotlar:\n")
    print(f"{davlat.title()}ning poyxatxi {davlat_info['potaxti']}\n")
    print(f"Hududdi:  {davlat_info['Hududi']}")
    print(f"Aholisi soni:  {davlat_info['Aholisi']}")
    print(f"Pul birligi {davlat_info['Pul birligi']}")



# endi tepadagi dasturga o'zgartirish kiritamiz yani foydalanuvchi so'ragan davlat haqida malumot chiqaramiz    


davlat_nomi = input("qaysi davlat haqida ma'lumot kerak kirirting: ")

davlatlar = {
      "o'zbekiston" : {
          "potaxti" : 'Toshkent',
          "Hududi" : '448 978 km²',
          "Aholisi" : '36,5 million kishi',
          "Pul birligi" : 'So‘m (UZS)',
      },

    "rossiya" : {
          "potaxti" : 'Moskva',
          "Hududi" : '17 098 246 km²',
          "Aholisi" : '145 million kishi',
          "Pul birligi" : 'Rubl (RUB))',
      },

    "amerika" : {
          "potaxti" : 'Vashington (Washington, D.C.)',
          "Hududi" : '9 833 517 km²',
          "Aholisi" : '340 million kishi',
          "Pul birligi" : 'AQSh dollari (USD)',
      },

    "turkiya" : {
          "potaxti" : 'Anqara (Ankara)',
          "Hududi" : '783 562 km',
          "Aholisi" : '86 million kishi',
          "Pul birligi" : 'Turk lirasi (TRY)',
      },
}

if davlat_nomi in davlatlar:
 info = davlatlar[davlat_nomi]
 print(f"{davlat_nomi} haqida ma'lumotlar:\n")
 print(f"{davlat_nomi.title()}ning poyxatxi {info['potaxti']}\n")
 print(f"Hududdi:  {info['Hududi']}")
 print(f"Aholisi soni:  {info['Aholisi']}")
 print(f"Pul birligi {info['Pul birligi']}")

else:
   print(f"{davlat_nomi} haqida ma'lumot mavjud emas")



# dunyodagi yaki adabiyot va tarixdagi 4 ta mashhur shaxlar haqidagi malumotni lugatlarda saqlaymiz va uni konsolga chiqaramiz


mashhur_shaxslar = {
   "Alisher Navoiy" : {
      "tug'ilgan yili" : 1441,
      "Tug‘ilgan joyi" : "Hirot (hozirgi Afg‘oniston hududi)",
      "Kasbi" : "Shoir, davlat arbobi, mutafakkir",
      "yashagan" : "60",

      "Asarlari yoki yutuqlari": [
            "O‘zbek adabiy tilining asoschisi",
            "Ko‘plab falsafiy va axloqiy asarlar yozgan",
            "She’riyat va adabiyot rivojiga katta hissa qo‘shgan",
            "Fors va turkiy tillarni solishtirgan ilmiy ishlar yaratgan"
      ]
   },  

    "Amir Temur" : {
      "tug'ilgan yili" : 1336,
      "Tug‘ilgan joyi" : "Kesh (hozirgi Shahrisabz, O‘zbekiston)",
      "Kasbi" : "Sarkarda, davlat arbobi, Temuriylar imperiyasi asoschisi",
      "yashagan" : "69",

      "Asarlari yoki yutuqlari": [
         "Temuriylar imperiyasini barpo etdi",
         "Samarqandni dunyoning eng go'zal poytaxtiga aylantirdi",
         "Harbiy va siyosiy tizimni mustahkamladi",
         "Ilm-fan, me'morchilik va san'atni rivojlantirdi"
      ]

   },

    "Zahiriddin Muhammad Bobur": {
        "tug'ilgan yili": 1483,
        "Tug‘ilgan joyi": "Andijon, Farg‘ona vodiysi, O‘zbekiston",
        "Kasbi": "Shoh, shoir, sarkarda va yozuvchi",
        "yashagan" : 47,

        "Asarlari yoki yutuqlari": [
            "Boburiylar imperiyasining asoschisi (Hindistonda)",
            "“Boburnoma” asarining muallifi – o‘z davrining noyob tarixiy manbasi",
            "Yirik sarkarda sifatida Hindistonni birlashtirishda muhim rol o‘ynagan",
            "Adabiyot, musiqa va san’at rivojiga katta hissa qo‘shgan"
        ],

    },

    "Mirzo Ulug‘bek": {
        "tug'ilgan yili": 1394,
        "Tug‘ilgan joyi": "Sultoniya shahri, Eron (Amir Temurning nabirasi)",
        "Kasbi": "Olim, astronom, matematik, davlat arbobi",
        "yashagan" : 55,

        "Asarlari yoki yutuqlari": [
            "Samarqandda Ulug‘bek rasadxonasini qurgan",
            "Yulduzlar jadvalini tuzgan — “Ziji Jadidi Kuragoniy” asari",
            "O‘sha davrda dunyodagi eng aniq astronomik o‘lchovlarni amalga oshirgan",
            "Temuriylar davrida ilm-fan va madaniyatni rivojlantirgan"
        ],

    }
}

mashhur_shaxslar = {
   "Alisher Navoiy": {
      "tug'ilgan yili": 1441,
      "Tug‘ilgan joyi": "Hirot (hozirgi Afg‘oniston hududi)",
      "Kasbi": "Shoir, davlat arbobi, mutafakkir",
      "yashagan": 60,
      "Asarlari yoki yutuqlari": [
         "O‘zbek adabiy tilining asoschisi",
         "Ko‘plab falsafiy va axloqiy asarlar yozgan",
         "She’riyat va adabiyot rivojiga katta hissa qo‘shgan",
         "Fors va turkiy tillarni solishtirgan ilmiy ishlar yaratgan"
      ]
   },

   "Amir Temur": {
      "tug'ilgan yili": 1336,
      "Tug‘ilgan joyi": "Kesh (hozirgi Shahrisabz, O‘zbekiston)",
      "Kasbi": "Sarkarda, davlat arbobi, Temuriylar imperiyasi asoschisi",
      "yashagan": 69,
      "Asarlari yoki yutuqlari": [
         "Temuriylar imperiyasini barpo etdi",
         "Samarqandni dunyoning eng go'zal poytaxtiga aylantirdi",
         "Harbiy va siyosiy tizimni mustahkamladi",
         "Ilm-fan, me'morchilik va san'atni rivojlantirdi"
      ]
   },

   "Zahiriddin Muhammad Bobur": {
      "tug'ilgan yili": 1483,
      "Tug‘ilgan joyi": "Andijon, Farg‘ona vodiysi, O‘zbekiston",
      "Kasbi": "Shoh, shoir, sarkarda va yozuvchi",
      "yashagan": 47,
      "Asarlari yoki yutuqlari": [
         "Boburiylar imperiyasining asoschisi (Hindistonda)",
         "“Boburnoma” asarining muallifi – o‘z davrining noyob tarixiy manbasi",
         "Yirik sarkarda sifatida Hindistonni birlashtirishda muhim rol o‘ynagan",
         "Adabiyot, musiqa va san’at rivojiga katta hissa qo‘shgan"
      ]
   },

   "Mirzo Ulug‘bek": {
      "tug'ilgan yili": 1394,
      "Tug‘ilgan joyi": "Sultoniya shahri, Eron (Amir Temurning nabirasi)",
      "Kasbi": "Olim, astronom, matematik, davlat arbobi",
      "yashagan": 55,
      "Asarlari yoki yutuqlari": [
         "Samarqandda Ulug‘bek rasadxonasini qurgan",
         "Yulduzlar jadvalini tuzgan — “Ziji Jadidi Kuragoniy” asari",
         "O‘sha davrda dunyodagi eng aniq astronomik o‘lchovlarni amalga oshirgan",
         "Temuriylar davrida ilm-fan va madaniyatni rivojlantirgan"
      ]
   }
}

for m_ism, m_info in mashhur_shaxslar.items():
    print(f"{m_ism} {m_info['tug\'ilgan yili']} yilda tug‘ilgan, "
          f"tug‘ilgan joyi {m_info['Tug‘ilgan joyi']}. "
          f"Kasbi: {m_info['Kasbi']}. "
          f"{m_info['yashagan']} yil yashagan.\n")

    print(f"{m_ism} ning asarlari yoki yutuqlari:")
    for malumot in m_info["Asarlari yoki yutuqlari"]:
        print(f" - {malumot}")
    print("\n")

