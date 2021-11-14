

users=[]
id=1

def addinguser():   
    global id
    name=input("Insert the name: ")
    surname=input("Insert the surname: ")
    email=input("Insert the email: ")
    

    user={
        'name':name,
        'surname':surname,
        'email':email,
        'id':id,
    }
    users.append(user)
    id=id+1

def showall():
    for user in users:
        print(f'{user["id"]} - {user["name"]} - {user["surname"]} - {user["email"]}')    

def deleteruser():
    delete=int(input("Write the id of User which you want to be deleted: "))
    for user in users:
        if delete==user["id"]:
            users.remove(user)

def updateuser():
    smth=int(input("Insert the Id of user you want to update: "))
    for user in users:
        if smth==user["id"]:
            newdate=input("Write new date,please: ")
            user["name"]=newdate
            






print(""""
-If you want to add an user, press: 1
-If you want to see all users, press: 2
-Ig you want to delete an user, press: 3
-if you want to update an user, press:4
"""
)



while True:    
    action=int(input("Write an option, what you want to reproduct: "))    
    if action==1:
        addinguser()
        
    elif action==2:
        showall()
    elif action==3:
        deleteruser()
    elif action==4:
        updateuser()
    else:
        break


