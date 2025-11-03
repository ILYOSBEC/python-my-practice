# 3 ta dostimni ismini ni lista yozib xabar yozaman

dostlarim = ["abror"], ["jasur"], ["dilshod"]

print("salom ", dostlarim[0] , " bugun bozorga boramizmi ", dostlarim[2] , " va " , dostlarim[1] , " sizlar ham bosozrga borasizlarmi" )

#sonlar degan list yaratamiz va ularni uistida turli xil arifmetik ammalar bajarb koramiz

sonlar = [112, 7123, 23.82, 299, 1000]

del sonlar[4]

sonlar.append("sarvar")

sonlar.insert(1427, "sunnat")

print(sonlar)
print(sonlar[0] + sonlar[3])

print(sonlar[1] - sonlar[3])

print(sonlar[0] * sonlar[1])

print(sonlar[3] / sonlar[2])


# t_shaxslar va z_shaxslar degan 2 ta royxat yaratamiz  va pop  bilan ishlaymiz 

t_shaxslar = ['Amir Temur', 'Albert Enshteyn', 'Islom Karimov', 'Mirzo ulug\'bek']

z_shaxslar = ['Elon Musk', 'Cristiano Ronaldo', 'Robert Downy Junior', 'Shavkat Mirziyoyev']

t_shaxs  = t_shaxslar.pop(0)

z_shaxs  = z_shaxslar.pop(1)

print('men tarixiy mashhur shaxslardan ', t_shaxs ,' bilan  va zamonaviy mashhur shaxslardan ',  z_shaxs , ' bilan uchrashishni xoxlar edim.')


# friend nomli bosh royxat yaratamiz va uni appent yordamida toldiramiz.  kela olmaydiganlarni remov orqali royxatdan chiqaramiz.

friends = []

friends.append('sarvar')
friends.append('jasur')
friends.append('abror')
friends.append('dilshod')
friends.append('jamshid')
friends.append('g\'olib')
friends.append('feruz')
friends.append('shamshod')
friends.append('aziz')
friends.append('nurbek')


friends.remove('jamshid')
friends.remove('nurbek')

print(friends)


# mehmonlar degan royxat yaratamiz va pop va appent yordaiidan royxatdan mehmonga kelgan sotlarni ismini sugurub olamiz

mehmonlar = friends.pop(0)
mehmonlar1 = friends.pop(1)
mehmonlar2 = friends.pop(2)
mehmonlar3 = friends.pop(3)

print( 'mehmonga kelgan do\'stlarim : ', mehmonlar , mehmonlar1, mehmonlar2, mehmonlar3   )


