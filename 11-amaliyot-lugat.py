# otam onam ukam akam va hokazu shunday lug'at yaratamiz va ular haqida kamida 3 ta malumot kiritamiz

otam = {
    "ism" : "Laziz",
    "yosh" : 41,
    "t_yil" : 1984
}

onam = {
    "ism" : "Oydin",
    "yosh" : 36,
    "t_yil" : 1989
}
men = {
    "ism" : "ilyosbek",
    "yosh" : 15,
    "t_yil" : 2010
}
ukam = {
    "ism" : "islom",
    "yosh" : 7,
    "t_yil" : 2018
}
akam = {
    "ism" : "asad",
    "yosh" : 18,
    "t_yil" : 2007
}

print(f"Mening olilam: otamning ismi {otam ["ism"]} {otam ["t_yil"]} yilda tug'ilganlar va hozirda {otam ["yosh"]} yoshda lar. va mening ismim {men ["ism"]} {men ["t_yil"]} yilda tug'ilganman va hozirda {men ["yosh"]} yoshdaman.")


# do'stlarimning sevimli taomlari haqida lugat yaratamiz

ali = {"taom" : "osh" }
dilshod = {"taom" : "somsa" }
sarvar = {"taom" : "sho'rva" }
jasur = {"taom" : "manti" }
anvar = {"taom" : "kabob" }

print(f"do'stlarimning sevimli taomlari: alining sevimli taomi {ali ["taom"]}, dilshodning sevimli taomi {dilshod ["taom"]}, sarvarning sevimli taomi {sarvar ["taom"]}")

# pythonda izohli lugat tuzamiz va shu kungacha o'rgangan 10 ta tamamni kiritaman

python_atamalar = {
    "1-atama": "if",
    "2-atama": "elif",
    "3-atama": "integer",
    "4-atama": "float",
    "5-atama": "else",
    "6-atama": "string",
    "7-atama": "in",
    "8-atama": "for",
    "9-atama": "n",
    "10-atama": "i"
}

print(f""" 
      Men shu paygacha o'rgangan pythondagi atamalar: {python_atamalar ["1-atama"]} ,
      {python_atamalar ["5-atama"]} va {python_atamalar ["2-atama"]}. va yana  
      {python_atamalar ["3-atama"]} , {python_atamalar ["4-atama"]} , {python_atamalar ["6-atama"]} ,
      {python_atamalar ["7-atama"]} va {python_atamalar ["8-atama"]} va {python_atamalar ["9-atama"]} ,
      {python_atamalar ["10-atama"]} kabilarni o'rgandim va kelajakda yana kop atamalarni o'rganaman.
        """)


# foydalanuvchidan biror so'z kirtishin i so'raymiz va agar lugatda mavjud bolmasa mavjud emas deganxabarni chiqaramiz 


kiriting = input("Kalit so'z kiriting: ")

lugat = {
    "integer": "butun son",
    "if": "agar",
    "or": "yoki",
    "string": "matn qiymat",
    "float": "son",
    "else": "aks holda"
}

print(lugat.get(kiriting , "Bizning lug‘atimizda bu so‘zning tarjimasi yo‘q"))








# tepadagini if else bilan qildim


soz_kiriting = input("Kalit so'z kirting: ")

lugat = {
    "integer" : "butun son",
    "if" : "agar",
    "or" : "yoki",
    "string" : "matn qiymat",
    "float" : "son",
    "else" : "aks holda",
}

if soz_kiriting in lugat:
    print(f"{soz_kiriting} ni tarjimasi {lugat[soz_kiriting]} degani")
else: 
  print(f"{soz_kiriting} so'zi lug'atda yo'q")    


