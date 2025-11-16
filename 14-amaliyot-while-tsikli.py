# foydalanuvchidan yoqtirgan kitobi nomini kiritishini soeraymiz va stop dep yozganda to'xtatamiz

s_kitob = "sevimli kitobingiz nomini kriting: "
s_kitob += 'chiqosh uchun "stop" dep yozing '

qiymat = ''

while qiymat != "stop" :
    qiymat = input(s_kitob)
if qiymat != "stop" :
    print(f" {qiymat}, ajoyib")


# foydalanuvchidan yoshini sraymiz va yoshiga qarab muzeyga kirish narxini aytamiz


muzeyga_kirish = "Yoshingizni kiriting (yoki 'chiqish' deb yozing): "

while True:
    qiymat_1 = input(muzeyga_kirish)

    if qiymat_1.lower() == 'chiqish':
        print("Dasturdan chiqdingiz.")
        break

    yosh = int(qiymat_1)

    if yosh <= 7:
        narx = 2000
    elif yosh <= 18:
        narx = 3000
    elif yosh <= 65:
        narx = 10000
    else:
        narx = 0

    print(f"Siz muzeyga kirish uchun {narx} so'm to'laysiz.\n")


#  tepadagini ishora korinishida ozgartiramiz

muzeyga_kirish = "Yoshingizni kiriting (yoki 'chiqish' deb yozing): "

ishora = True

while ishora:
    qiymat_1 = input(muzeyga_kirish)

    if qiymat_1.lower() == 'chiqish':
        ishora = False
        print("Dasturdan chiqdingiz.")
        break

    yosh = int(qiymat_1)

    if yosh <= 7:
        narx = 2000
    elif yosh <= 18:
        narx = 3000
    elif yosh <= 65:
        narx = 10000
    else:
        narx = 0

    print(f"Siz muzeyga kirish uchun {narx} so'm to'laysiz.\n")


# amaliyotda berilgan dastur kodini xatolarini togrlaymiz


print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing)"

while True:
    qiymat = input(savol)
    if qiymat =='exit':
     print("dasturdan chiqdingiz")
     break

    qiymat = float(qiymat)

    if qiymat < 0:
       print("iltimos, musbat son kiriting")
       continue

    print (f"{qiymat} ning ildizı {qiymat**0.5} ga teng")

 
                