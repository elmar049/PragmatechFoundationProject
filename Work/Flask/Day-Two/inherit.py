class Worker:
    def __init__(self,ad, soyad):
        self.name=ad
        self.surname=soyad

    def Showdetail(self):   
        return self    





class Developer(Worker):
    def __init__(self, ad, soyad, dil):
        # self.name=ad
        # self.surname=soyad
        super().__init__(ad, soyad)
        self.lang=dil



class Accounter(Worker):
    def __init__(self, ad, soyad, tecrube):
        # self.name=ad
        # self.surname=soyad
        super().__init__(ad, soyad)    #sual- burdaki parameter Superden gelir? yoxsa ele current Classdaki ad soyaddi, yani  burdaki parametri sile bilerem?
        self.experience=tecrube




class Volunter(Worker):
    def __init__(self, ad, soyad, zaman):
        # self.name=ad
        # self.surname=soyad
        super().__init__(ad,soyad)
        self.time=zaman


x=Developer("Elmar", "Mammadov", "python")
x.



