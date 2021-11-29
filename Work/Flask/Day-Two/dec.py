def Murad():
    return "Cup "

def Rehman():
    return "Phone "    


    

def Fezail(anyfun):
    def onemorefun(): #zachem na ewe odna fukcnia tut, esli mojno bezz nee oboytis
        x=anyfun()   # pricem tut et
        result=anyfun() + "adding new info"
        return result   
    return onemorefun    


decorate= Fezail(Murad)
print(decorate)  #pcmu zdes decorate so skobkami

##############raznicaaaaa


# def Fezail (anyfun):
#     result=anyfun() + "adding new info"
#     return result

# decorate= Fezail(Murad)
# print(decorate)     # zdes eqo mojno zaprintit bez skobok posle decorate