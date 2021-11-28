student=[]
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'





class Registration():
    def __init__(self, name, surname, email, phone, password, melumat):
        self.name=name
        self.surname=surname
        self.email=email
        self.phone=phone
        self.password=password
        self.melumat=melumat


    def show (self):
        print(f'{self.name}  {self.surname}  {self.email}  {self.phone}  {self.password}  {self.melumat}')

    def getusername(self):
        self.name=input(str("Adi daxil edin: "))
        if self.name == "":
            print("Doldurmaq Zeruridir")
        else:
            print(self.name)   

    
    def getsurname(self):
        self.surname=input(str("Familiyani daxil edin: "))
        if self.surname == "":
            print("Doldurmaq Zeruridir")
        else:
            print(self.surname) 


    def getpasssword(self):
        self.password=input(str("Parolu daxil et: "))
        
        if len(self.password) < 8:
            print('Minimum 8 xarakterden ibaret olmalidir qaqash')
                    
        if len(self.password) > 20:
            print('Maksimum 20 xarakterden ibaret olmalidir')
    

        if not any(char.isdigit() for char in self.password):
            print('Password should have at least one numeral')
           
            
        if not any(char.isupper() for char in self.password):
            print('Password should have at least one uppercase letter')
          
            
        if not any(char.islower() for char in self.password):
            print('Password should have at least one of the lowercase letter')
            


    def getemail(self):
        self.email=input(str("Insert the email: "))
        if(re.fullmatch(regex, self.email)):
            print("Valid Email")
        else:
            print("Invalid Email")





    def getnumber(self):
        self.number=input(str("Nomreni daxil edin: +994"))
        if len(self.number)!=9:
            print("Qeyd etdiyniz nomre 9 reqemli olmalidir")
            True

        if not all( chart.isdigit() for chart in self.number): 
            print("Qeyd etdiyniz nomre yalniz reqemdeb ibaret olmalidir")
            True
        
        elif self.number.startswith("55", 0, 2):
            print("Prefiks duzdu")
            True

        elif self.number.startswith("50", 0, 2):
            print("Prefiks duzdu")
            True

        elif self.number.startswith("51", 0, 2):
            print("Prefiks duzdu")
            True
        elif self.number.startswith("70", 0, 2):
            print("Prefiks duzdu")
            True
        elif self.number.startswith("77", 0, 2):
            print("Prefiks duzdu")
            True
        else:
            print("nomreni duzgun qeyd edin")
            



        # numerrr=str(input("type a number: +994 "))
        # if numerrr[0]!="5" or "7":
        #     print(" operator kod sefdir")
        # elif numerrr[1]!="0" or "1" or "5" or "7":
        #     print(" operator kod sefdir")
        # elif len(numerrr) == 9:
        #     print(f'{ +994} {numerrr}')
        # else:
        #     print("Sefh daxil edilib nomre")    
               


user=Registration( 'elmar', "eee", "eee", "fef", "fef", "melumat")
user.getusername()
user.getsurname()
user.getemail()
user.getnumber()
user.getpasssword()



# def showallusers():
#     for oneuser in student:
#         oneuser.show()

