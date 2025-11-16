# 1)  User class ni yaratamiz va famliliya ism yosh xullas odatdan ijtimoiy tarmoqlar soraydigan ma'lumotlarni so'raymiz
# 2) class ga bir nechta methodlar qo'shamiz masalan get_info
# 3) klassdan bir nechta obeyklar yaratamiz va methodlariga murojaat qilamiz

class User:
    def __init__(self, ism , familiya , username ,  yosh , tyil , email , traqam ):
        self.ism = ism
        self.familiya = familiya
        self.username = username
        self.yosh = yosh
        self.tyil = tyil
        self.email = email
        self.traqam = traqam


    def get_name(self):
        """foydalanuvchining ismini qaytaradi""" 
        return self.ism  
    


    def get_lastname(self):
        """foydalanuvchining familiyasini qaytaradi""" 
        return self.familiya  



    def get_username(self):
        """foydalanuvchining username ni qaytaradi""" 
        return self.username  



    def get_age(self):
        """foydalanuvchining yoshini qaytaradi""" 
        return self.yosh  



    def get_born_year(self):
        """foydalanuvchining tu'gilgan yilini qaytaradi""" 
        return self.tyil                  


    def get_telephone_number(self):
        """foydalanuvchining telfon raqamini qaytaradi""" 
        return self.traqam   
    

    def work(self):
        """foydalanuvchini kasbini qaytaradi"""
        pass

    

    def bio(self):
        """foydalanuvchining biosini qaytaradi"""
        pass
    


        
    def get_info(self):
        print(f"\nFoydalanuvchi haqida ma'lumotlar:\n\n")
        print(f"foydalanvchi: {self.username}")
        print(f"Ismi: {self.ism}")
        print(f"Familiyasi: {self.familiya}")
        print(f"Yoshi: {self.yosh}")
        print(f"Tug'ilgan yili: {self.tyil}")
        print(f"Emaili: {self.email}")
        print(f"Telefon raqami: {self.traqam}\n")





Foydalanuvchi_1 = User("ilyosbek" , "ro'ziyev" , "ILYOSBEC" , 15 , 2010 , "ilyosbekruzuyev@gmail.com" ,  "+998 99 134 92 07")   
Foydalanuvchi_2 = User("jasur" , "azamtov" , "Azamat_off" , 20 , 2005 , "azamatoff096@gmail.com" ,  "+998 91 533 00 56")   
Foydalanuvchi_3 = User("dilshod" , "toshtemirov" , "Dima_007" , 18 , 2007 , "dilshodjon0909@gmail.com" ,  "+998 93 156 72 07")   
Foydalanuvchi_4 = User("sarvar" , "qodirov" , "Sarik" , 17 , 2008 , "sarvarbekqodirov@gmail.com" ,  "+998 90 134 00 07")   
 

print(Foydalanuvchi_1.get_info())
print(Foydalanuvchi_2.get_info())
print(Foydalanuvchi_3.get_info())
print(Foydalanuvchi_4.get_info())





        
