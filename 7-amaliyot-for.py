# ismlar degan royxat tuzmiz va ichiga 5 ta dan ortiq xabar yozamiz

ismlar = ["alisher", "ilyosbec", "jasur", "dilshod", "sherzod", "qobil", "ozod"]

for ism  in ismlar:
  print("salom ", ism)

  # sonlar degan royxat yartamiz va har bir sonning kubi yangi qatordan chiqadi
  
  sonlar = list(range(10,101))

  for son in sonlar:


    print("bu sonning kubi: ", son**2 , " ga teng boladi." )


#  foydalanuvchidan kinolarni sorab uni kinolar degan royxatga kiritamiz

kino1 = input("birinchi kino nomini kiring: ")
kino2 = input("ikkinchi kino nomini kiring: ")
kino3 = input("uchinchi kino nomini kiring: ")
kino4 = input("to'rtinchi kino nomini kiring: ")
kino5 = input("beshinchi kino nomini kiring: ")

kinolar = [kino1 , kino2, kino3, kino4, kino5 ]

print("sizning sevimli kinolaringiz: ", kinolar)


# foydalanuvchildan nechta odam bilan suhbatlashgani va ularni ismini sorab konsolga chiqaramiz

uchrashgan_insonlar = int(input("bugun nechta odam bilan uchrashdingiz: "))

odamlar = []


for i in range(1, uchrashgan_insonlar+1):
    ism = input(f"{i}-suhbat qilgan odamingiz kim edi: ")
    odamlar.append(ism)



print("\nBugun suhbat qilgan odamingizlar ro'yxati:")
print(odamlar)    

