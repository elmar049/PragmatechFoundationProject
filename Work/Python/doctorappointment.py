NewUser=input('Yeni Istifadecini Elave etmek ucun: ')
NewSurname=input('Zehmet olmasa soyadini qeyd edesiniz: ')
NewId=input('Zehmet olmasa istifadecinin ID-sini qeyd edin:')



yeniuser={'Name':NewUser, 'Surname':NewSurname, 'ID': NewId}
print(yeniuser)

users=[yeniuser]
users.append(yeniuser)
print(users)





# yeniuser={'Name': users.append(NewUser), 'Surname': users.append(NewSurname), 'ID': users.append(NewId)}
# print(yeniuser)


