# o'zgaruvchilar yaratamiz

kocha = "bog'bon"
mahalla = "sog'bon"
tuman = "bodomzor"
viloyat = "samarqand"

print(kocha , "ko'chasi, " , mahalla, "mahallasi, ", tuman, "tumani, ", viloyat, "viloyati")



# input orqali foydalanuvchini manzilini so'raymiz


kocha = input("ko'changiz nomini kiriting: ")
mahalla = input("mahallangiz nomini kiriting: ")
tuman = input("tumaningiz nomini kiriting: ")
viloyat = input("viloyatingiz nomini kiriting: ")

print("manzilingiz:", kocha , "ko'chasi, " , mahalla, "mahallasi, ", tuman, "tumani, ", viloyat, "viloyati")


# manzil degan ozgaruvchi yaratamiz va    larni siznab koramiz

manzil = f" 'manzilingiz:' {kocha}  'ko'chasi, '   {mahalla}  'mahallasi, '  {tuman}  'tumani, ', {viloyat} 'viloyati' "

print(manzil.title())

print(manzil.upper())

print(manzil.capitalize())

print(manzil.lower())

