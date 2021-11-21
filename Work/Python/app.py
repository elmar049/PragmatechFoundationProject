# def ShowMyInfo(name, proff, petName): 
#     print('My name is'+ name)  
#     print('My profesion is'+ proff)
#     print(f"The pet {petName} i have is")
    

    

# ShowMyInfo('Rahman', 'Stuardessa')




# def CountNumbers(*nums):
#     print(nums)

# CountNumbers(1,2,4,6,7,2,1)


# yas=28

# def YasiGoster():
#     print(yas)


# def YeniYas():
#     global yas 
#     yas=41
#     print(yas)


# YasiGoster()
# YeniYas()
# print(yas)


# yas=input('yasini daxil et: ')
# if int(yas)<25:
#     print('kef ele')
# elif 25<int(yas)<35:
#     print('Terpenmirsen hele?')

# elif 35<int(yas)<45:
#     print('Uwaq boyuyur')

# else:
#     print('kefen hazirdi')


# //
# zaman=int(input('Nece saat mawin sururduz?'))
# distance=int(input('suretiniz nece olub'))
# km=distance*zaman
# ml=km/1.6

# print(f"Siz bu elde olunan melumatlarla {km} kilomet qeht ede bildiniz")
# print(f"hansiki mile cevirilse, {ml} mil eleyir")


adlar=[
    'Fezail',
    'Rehman',
    'Elmar',
    'Sebuhi',
    'Aysel',
    'Murad',
    'Vesile',
    'Ravi'
]

 #Butun adlari ekrana cap eden metod yazin adlariGoster()
# Listin cut yerde duran elementlerini gosteren metod yazin cutYerdekiler()
# Listi elifba sirasina gore siralayan metod yazin listiSirala()


def adlariGoster():
     for addd in range(len(adlar)):
         print(adlar[addd])

adlariGoster()


def cutYerdekiler():
    for i in range(len(adlar)):
        i=i+1;
        if i%2==0:
            print(adlar[i])
        else:
             print(adlar)

cutYerdekiler()
