# foydalanuvchidan yoshi va ismini so'rab uni tugilgan yilini topamiz

def yosh_hissobla(ism, yosh, h_yil=2025):
    """Ismini chiqaradigan funksiya"""
    print(f"Assalomu alaykum, {ism} sizning tugilgan yilingiz {h_yil-yosh}")

ism_k = input("ismingizni kiriting: ")
yosh_k = int(input("yoshingizni kiriting: "))
yosh_hissobla(ism_k , yosh_k)


# foydalanuvchidan son olib uni nkvadrati va kubini korsatuvchi funksiya qilamiz

def m_hissobla(misol):
    """siz krirtgan sonni kubi va kvadratini topib beradi"""
    print(f"{misol} ning kvadrati {misol**2} va kubi {misol**3} ga teng")

m_kirit = int(input("istalgan sonni kiriting: "))    
m_hissobla(m_kirit)


# foydalanuvchidan son olamiz va uni juft yoki toqligini konsilga chiqaramiz

def m_hissobla2(misol):
    """isz kiritgan sonni toq yiki juftligini aniqlab beradi"""
    if misol % 2 == 0:
     print(f"siz kiritgan son jusft soon")
    else:
      print("siz kiritgan son toq son")

m_kirit = int(input("istalgan sonni kiriting: "))  
m_hissobla2(m_kirit)    


#foydalanuvchidan 2 ta son olamiz va ulardan kattasini ekranga chiqaramiz agar teng bolsa tesng deymiz

def son(raqam1 , raqam2):
   """"siz kiritgan sonni tkatta  yoki tengligini korsatadi"""
   if raqam1 > raqam2   :
      print(f"siz kiritgan sonlardan {raqam1} katta")
   elif raqam2 > raqam1 :
      print(f"siz kiritgan sonlardan {raqam2} katta") 
   else:
      print("siz kiritgan sonlar teng")   

raqam_k1 = int(input("birinchi raqamni kiriting: "))
raqam_k2 = int(input("ikkinchi raqamni kiriting: "))

son(raqam_k1 , raqam_k2)



# foydalanuvchidan x va y sonlarni olamiz va ularni xy qilamiz yani darjaga oshiramiz


def daraja_osh(d_raqam1 , d_raqam2) :
   """siz kirtigan 2 ta raqamni darajaga oshirib beruvchi dastur"""
   print(f"{d_raqam1} va {d_raqam2} ni darajaga oshirilgani {d_raqam1**d_raqam2} bo'ladi ")

d_raqam_k1 = int(input("birinchi son: "))
d_raqam_k2 = int(input("ikkinchi son: "))

daraja_osh(d_raqam_k1 , d_raqam_k2)


#quydagi funksiyaga 2 ta standart raqam belgilab ishlatamiz

def daraja_osh2(son1):
   "siz kiritgan sonni 10 va 15 darajasiga oshirib beradi"
   print(f"{son1} ning 10 ga va 15 ga daraja oshgani {son1**10} va {son1**15}")

son1_k = int(input("istalgan son kiriting: "))   

daraja_osh2(son1_k)


# foydalanuvchidan son olamiz va uni 2 dan 10 gacha bolgan sonlar oraligida qoldiqsiz bolinadiganlarni konsolga chiqaramiz

def misol(bolinuvchi ):
   """siz kritgan sonni 2-10 rasida bolinadiganini konsolga chiqaramiz"""
   for  boluvchi in range(2,11):
    if bolinuvchi % boluvchi == 0:
      print(f"{bolinuvchi} ga {boluvchi}  qoldiqsiz bo'linadi ")


bolinuvchi_k = int(input("son kiriting: "))

misol(bolinuvchi_k )


