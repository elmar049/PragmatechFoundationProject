
from reg import Registration, student, showallusers
while True:
    emr=input(str("Yeni user daxil olunsun: (y/n) "))
    if emr== "y":
        name=input(str("Insert the name of user: "))

        surname=input(str("Insert the surname of user: "))

        email= input(str("Insert the email of User: "))

        number=input(str("Insert the number of user: "))
    
        password=input(str("Insert the password of user: "))

        melumat=input(str("Insert the info about the user: "))

        user=Registration( name, surname, email, number, password, melumat)
        name.getusername()
        surname.getsurname()
        email.getemail()
        number.getnumber()
        password.getpassword()
        user.getpassword()   #or here should be only user

       

        
        student.append(user)
        showallusers()

    else:
        break


