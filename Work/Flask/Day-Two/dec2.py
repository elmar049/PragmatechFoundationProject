def Fezail(anyfun):
    def onemorefun():
        result=anyfun() + "adding new info"
        return result   
    return onemorefun 




@Fezail  #eto decokartor mir metoda elave funksiya elave edir i mojno li eto zamenit Fezail(Murad)
def Murad():
    return "Cup "   

print(Murad())    